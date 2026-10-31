import math
import shutil
import subprocess
import tempfile
from pathlib import Path

from studio.drawing import create_frame, draw_character


def build_test_video(output_path="test_animation.mp4"):
    ffmpeg = shutil.which("ffmpeg")

    if not ffmpeg:
        raise RuntimeError("FFmpeg is not installed.")

    fps = 24
    duration = 5
    total_frames = fps * duration

    with tempfile.TemporaryDirectory() as temp:
        frame_dir = Path(temp)

        for frame_number in range(total_frames):
            t = frame_number / total_frames

            image = create_frame()

            bobo_x = int(350 + 500 * t)
            rexy_x = int(1250 - 350 * t)

            bounce = abs(math.sin(t * math.pi * 6)) * 35

            draw_character(
                image, "bobo", bobo_x, int(650 - bounce)
            )
            draw_character(
                image, "rexy", rexy_x, 650, 0.8
            )

            image.save(
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
                str(Path(output_path).resolve())
            ],
            check=True
        )

    return output_path
