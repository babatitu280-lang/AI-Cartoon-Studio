import tempfile
import subprocess
from pathlib import Path

from PIL import Image

from studio.video_exporter import export_video


def main():
    with tempfile.TemporaryDirectory() as temp:
        folder = Path(temp)
        frames_dir = folder / "frames"
        frames_dir.mkdir()

        # Create 5 temporary test frames
        for number in range(1, 6):
            image = Image.new(
                "RGB",
                (320, 180),
                (number * 40, 100, 180)
            )

            image.save(
                frames_dir / f"frame_{number:06d}.png"
            )

        output = folder / "test_video.mp4"

        result = export_video(
            frames_dir,
            output,
            fps=5
        )

        assert result.is_file()
        assert result.stat().st_size > 0

        # Verify that FFmpeg can read the exported video
        check = subprocess.run(
            [
                "ffprobe",
                "-v", "error",
                "-show_entries", "format=duration",
                "-of", "default=noprint_wrappers=1:nokey=1",
                str(output)
            ],
            capture_output=True,
            text=True,
            check=True
        )

        assert float(check.stdout.strip()) > 0

        print("Video exporter test passed!")


if __name__ == "__main__":
    main()
