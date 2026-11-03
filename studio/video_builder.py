
import shutil
import subprocess
from pathlib import Path

from studio.asset_registry import get_character_asset
from studio.character_animation import Keyframe
from studio.scene_animator import render_scene_animation


def build_test_video(output_path="test_animation.mp4"):
    ffmpeg = shutil.which("ffmpeg")
    if not ffmpeg:
        raise RuntimeError("FFmpeg is not installed.")

    root = Path(__file__).resolve().parent.parent

    bobo = get_character_asset("bobo", "bobo.png")
    rexy = get_character_asset("rexy", "rexy.png")

    background = root / "assets" / "backgrounds" / "test_background.png"
    if not background.is_file():
        raise FileNotFoundError(
            f"Background image not found: {background}"
        )

    output_path = Path(output_path).resolve()
    output_path.parent.mkdir(parents=True, exist_ok=True)

    import tempfile

    with tempfile.TemporaryDirectory() as temp:
        frame_dir = Path(temp) / "frames"

        bobo_frames = render_scene_animation(
            background,
            bobo,
            [
                Keyframe(0, 250, 500),
                Keyframe(2.5, 800, 450, rotation=8),
                Keyframe(5, 1100, 500),
            ],
            frame_dir / "bobo",
            duration=5,
            fps=24,
        )

        # Render Rexy separately, then composite both characters
        # into the same background for each output frame.
        rexy_frames = render_scene_animation(
            background,
            rexy,
            [
                Keyframe(0, 1300, 500),
                Keyframe(2.5, 1000, 500, rotation=-8),
                Keyframe(5, 750, 500),
            ],
            frame_dir / "rexy",
            duration=5,
            fps=24,
        )

        from PIL import Image

        combined_dir = frame_dir / "combined"
        combined_dir.mkdir(parents=True, exist_ok=True)

        for index, (bobo_frame, rexy_frame) in enumerate(
            zip(bobo_frames, rexy_frames)
        ):
            image = Image.open(bobo_frame).convert("RGBA")
            rexy_image = Image.open(rexy_frame).convert("RGBA")
            image.alpha_composite(rexy_image)

            image.convert("RGB").save(
                combined_dir / f"frame_{index:06d}.png"
            )

        subprocess.run(
            [
                ffmpeg, "-y",
                "-framerate", "24",
                "-i", str(combined_dir / "frame_%06d.png"),
                "-c:v", "libx264",
                "-pix_fmt", "yuv420p",
                "-movflags", "+faststart",
                str(output_path),
            ],
            check=True,
        )

    return str(output_path)
