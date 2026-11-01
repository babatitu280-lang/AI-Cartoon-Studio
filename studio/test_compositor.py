import tempfile
from pathlib import Path

from PIL import Image

from studio.compositor import composite_scene


def main():
    with tempfile.TemporaryDirectory() as temp:
        folder = Path(temp)

        background = folder / "background.png"
        character = folder / "character.png"
        output = folder / "output.png"

        # Temporary background for testing
        Image.new(
            "RGBA",
            (1920, 1080),
            (100, 150, 200, 255)
        ).save(background)

        # Temporary transparent character-shaped test image
        Image.new(
            "RGBA",
            (100, 200),
            (255, 180, 0, 255)
        ).save(character)

        composite_scene(
            background,
            [{
                "path": character,
                "x": 500,
                "y": 400,
                "height": 300
            }],
            output
        )

        result = Image.open(output)

        assert result.size == (1920, 1080)
        assert result.getpixel((510, 410)) == (255, 180, 0, 255)

        print("Compositor test passed!")


if __name__ == "__main__":
    main()
