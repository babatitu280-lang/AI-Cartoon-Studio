import json
from pathlib import Path

from studio.script_parser import validate_episode_script


def run_test():
    script_path = (
        Path(__file__).resolve().parent.parent
        / "assets"
        / "example_episode.json"
    )

    with script_path.open("r", encoding="utf-8") as file:
        script = json.load(file)

    assert validate_episode_script(script) is True
    print("Episode script test passed!")


if __name__ == "__main__":
    run_test()
