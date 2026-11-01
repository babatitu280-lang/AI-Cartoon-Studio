import tempfile
from pathlib import Path

from PIL import Image

from studio.character_animation import Keyframe
from studio.scene_animator import render_scene_animation


def main():
    with tempfile.TemporaryDirectory() as temp:
        folder = Path(temp)

        background = folder / "background.png"
        character = folder / "character.png"
        output_dir = folder / "frames"

        Image.new(
            "RGBA", (640, 360), (80, 120, 180, 255)
        ).save(background)

        Image.new(
            "RGBA", (80, 100), (255, 180, 0, 255)
        ).save(character)

        keyframes = [
            Keyframe(0, 100, 100),
            Keyframe(1, 300, 100)
        ]

        frames = render_scene_animation(
            background,
            character,
            keyframes,
            output_dir,
            duration=1,
            fps=2
        )

        assert len(frames) == 2
        assert all(frame.is_file() for frame in frames)

        print("Scene animator test passed!")


if __name__ == "__main__":
    main()
