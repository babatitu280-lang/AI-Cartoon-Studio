import tempfile
from pathlib import Path

from PIL import Image

from studio.character_animation import Keyframe
from studio.frame_renderer import render_character_frame


def main():
    with tempfile.TemporaryDirectory() as temp:
        folder = Path(temp)

        background = folder / "background.png"
        character = folder / "character.png"
        output = folder / "frames" / "frame_000001.png"

        Image.new(
            "RGBA", (640, 360), (80, 120, 180, 255)
        ).save(background)

        Image.new(
            "RGBA", (80, 100), (255, 180, 0, 255)
        ).save(character)

        keyframes = [
            Keyframe(0, 100, 100),
            Keyframe(2, 300, 100)
        ]

        result = render_character_frame(
            background,
            character,
            keyframes,
            1,
            output
        )

        assert result.is_file()

        rendered = Image.open(result)
        assert rendered.size == (640, 360)

        print("Frame renderer test passed!")


if __name__ == "__main__":
    main() 
