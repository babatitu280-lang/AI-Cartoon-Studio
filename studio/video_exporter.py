from pathlib import Path
import subprocess


def export_video(
    frames_dir,
    output_path,
    fps=24
):
    frames_dir = Path(frames_dir)
    output_path = Path(output_path)

    if not frames_dir.is_dir():
        raise FileNotFoundError("Frames folder not found.")

    if fps <= 0:
        raise ValueError("FPS must be positive.")

    frames = sorted(frames_dir.glob("frame_*.png"))

    if not frames:
        raise ValueError("No animation frames found.")

    output_path.parent.mkdir(
        parents=True,
        exist_ok=True
    )

    command = [
        "ffmpeg",
        "-y",
        "-framerate", str(fps),
        "-i", str(frames_dir / "frame_%06d.png"),
        "-c:v", "libx264",
        "-pix_fmt", "yuv420p",
        "-movflags", "+faststart",
        str(output_path)
    ]

    subprocess.run(command, check=True)

    if not output_path.is_file():
        raise RuntimeError("Video export failed.")

    return output_path
