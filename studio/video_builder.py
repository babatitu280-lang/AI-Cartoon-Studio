
import math
import shutil
import subprocess
import tempfile
from pathlib import Path

from PIL import Image, ImageDraw

from studio.asset_registry import get_character_asset
from studio.character_animation import Keyframe, animate_character


def paste_character(background, character_path, keyframes, current_time):
    character = Image.open(character_path).convert("RGBA")
    motion = animate_character(keyframes, current_time)

    width = max(1, round(character.width * motion["scale_x"]))
    height = max(1, round(character.height * motion["scale_y"]))

    character = character.resize(
        (width, height), Image.Resampling.LANCZOS
    )
    character = character.rotate(
        motion["rotation"],
        resample=Image.Resampling.BICUBIC,
        expand=True,
    )

    background.alpha_composite(
        character,
        (round(motion["x"]), round(motion["y"])),
    )


def build_test_video(output_path="test_animation.mp4"):
    ffmpeg = shutil.which("ffmpeg")
    if not ffmpeg:
        raise RuntimeError("FFmpeg is not installed.")

    bobo = get_character_asset("bobo", "bobo.png")
    rexy = get_character_asset("rexy", "rexy.png")

    fps = 24
    duration = 5
    total_frames = fps * duration

    bobo_keys = [
        Keyframe(0, 250, 500),
        Keyframe(2.5, 800, 450, rotation=8),
        Keyframe(5, 1100, 500),
    ]

    rexy_keys = [
        Keyframe(0, 1300, 500),
        Keyframe(2.5, 1000, 500, rotation=-8),
        Keyframe(5, 750, 500),
    ]

    output_path = Path(output_path).resolve()
    output_path.parent.mkdir(parents=True, exist_ok=True)

    with tempfile.TemporaryDirectory() as temp:
        frame_dir = Path(temp)

        for frame_number in range(total_frames):
            current_time = frame_number / fps

            background = Image.new(
                "RGBA", (1920, 1080), (150, 205, 235, 255)
            )
            draw = ImageDraw.Draw(background)
            draw.rectangle(
                (0, 750, 1920, 1080),
                fill=(105, 165, 95, 255),
            )

            paste_character(
                background, bobo, bobo_keys, current_time
            )
            paste_character(
                background, rexy, rexy_keys, current_time
            )

            background.convert("RGB").save(
                frame_dir / f"frame_{frame_number:06d}.png"
            )

        subprocess.run(
            [
                ffmpeg, "-y",
                "-framerate", str(fps),
                "-i", str(frame_dir / "frame_%06d.png"),
                "-c:v", "libx264",
                "-pix_fmt", "yuv420p",
                "-movflags", "+faststart",
                str(output_path),
            ],
            check=True,
        )

    return str(output_path)
