# AI Cartoon Studio
# MP4 video rendering engine

import subprocess
from pathlib import Path


def export_mp4(
    frames_folder,
    output_file,
    fps=24,
    width=1920,
    height=1080
):
    frames_folder = Path(frames_folder)
    output_file = Path(output_file)

    if not frames_folder.exists():
        raise FileNotFoundError("Frames folder does not exist.")

    frame_pattern = str(
        frames_folder / "frame_%06d.png"
    )

    output_file.parent.mkdir(
        parents=True,
        exist_ok=True
    )

    command = [
        "ffmpeg",
        "-y",
        "-framerate", str(fps),
        "-i", frame_pattern,
        "-vf",
        f"scale={width}:{height}:force_original_aspect_ratio=decrease,"
        f"pad={width}:{height}:(ow-iw)/2:(oh-ih)/2",
        "-c:v", "libx264",
        "-pix_fmt", "yuv420p",
        "-movflags", "+faststart",
        str(output_file)
    ]

    subprocess.run(
        command,
        check=True
    )

    return output_file


if __name__ == "__main__":
    print("AI Cartoon Studio MP4 renderer is ready.")
