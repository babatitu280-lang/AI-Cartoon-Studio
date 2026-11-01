
from pathlib import Path
import subprocess


def combine_video_audio(
    video_path,
    audio_path,
    output_path
):
    video_path = Path(video_path)
    audio_path = Path(audio_path)
    output_path = Path(output_path)

    if not video_path.is_file():
        raise FileNotFoundError("Video file not found.")

    if not audio_path.is_file():
        raise FileNotFoundError("Audio file not found.")

    output_path.parent.mkdir(
        parents=True,
        exist_ok=True
    )

    command = [
        "ffmpeg",
        "-y",
        "-i", str(video_path),
        "-i", str(audio_path),
        "-map", "0:v:0",
        "-map", "1:a:0",
        "-c:v", "copy",
        "-c:a", "aac",
        "-b:a", "192k",
        "-shortest",
        "-movflags", "+faststart",
        str(output_path)
    ]

    subprocess.run(command, check=True)

    if not output_path.is_file() or output_path.stat().st_size == 0:
        raise RuntimeError("Final video creation failed.")

    return output_path
