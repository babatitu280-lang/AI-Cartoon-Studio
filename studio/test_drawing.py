from pathlib import Path
from PIL import Image

from studio.drawing import create_test_frame


def run_test():
    output = Path("test_frame.png")

    create_test_frame(str(output))

    assert output.exists(), "Frame was not created"

    with Image.open(output) as image:
        assert image.size == (1920, 1080)
        assert image.format == "PNG"

    output.unlink()
    print("Drawing test passed!")


if __name__ == "__main__":
    run_test()
