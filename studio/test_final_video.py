
import tempfile
import subprocess
from pathlib import Path

from studio.final_video import combine_video_audio


def main():
    with tempfile.TemporaryDirectory() as temp:
        folder = Path(temp)

        video = folder / "test_video.mp4"
        audio = folder / "test_audio.wav"
        output = folder / "final_video.mp4"

        # Generate a temporary test video.
        subprocess.run([
            "ffmpeg", "-y",
            "-f", "lavfi",
            "-i", "color=c=blue:s=320x180:r=24:d=2",
            "-c:v", "libx264",
            "-pix_fmt", "yuv420p",
            str(video)
        ], check=True, capture_output=True)

        # Generate a temporary test audio track.
        subprocess.run([
            "ffmpeg", "-y",
            "-f", "lavfi",
            "-i", "sine=frequency=440:duration=2",
            "-c:a", "pcm_s16le",
            str(audio)
        ], check=True, capture_output=True)

        result = combine_video_audio(
            video,
            audio,
            output
        )

        assert result.is_file()
        assert result.stat().st_size > 0

        print("Final video test passed!")


if __name__ == "__main__":
    main()
