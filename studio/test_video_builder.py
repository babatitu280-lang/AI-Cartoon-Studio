from pathlib import Path
import shutil

from studio.video_builder import build_test_video


def run_test():
    if not shutil.which("ffmpeg"):
        raise RuntimeError("FFmpeg is not available.")

    output = Path("test_animation.mp4")

    build_test_video(str(output))

    assert output.exists(), "MP4 was not created."
    assert output.stat().st_size > 0, "MP4 is empty."

    print("MP4 video test passed!")


if __name__ == "__main__":
    run_test()
