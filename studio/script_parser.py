import json
from pathlib import Path


def load_episode_script(file_path):
    path = Path(file_path)

    if not path.is_file():
        raise FileNotFoundError(f"Script not found: {path}")

    with path.open("r", encoding="utf-8") as file:
        script = json.load(file)

    validate_episode_script(script)
    return script


def validate_episode_script(script):
    if not isinstance(script, dict):
        raise ValueError("Episode script must be an object.")

    if not script.get("title"):
        raise ValueError("Episode title is required.")

    scenes = script.get("scenes")

    if not isinstance(scenes, list) or not scenes:
        raise ValueError("At least one scene is required.")

    for number, scene in enumerate(scenes, start=1):
        if not isinstance(scene, dict):
            raise ValueError(f"Scene {number} must be an object.")

        if not scene.get("name"):
            raise ValueError(f"Scene {number} needs a name.")

        duration = scene.get("duration")

        if not isinstance(duration, (int, float)) or duration <= 0:
            raise ValueError(f"Scene {number} has an invalid duration.")

        if not isinstance(scene.get("actions", []), list):
            raise ValueError(f"Scene {number} actions must be a list.")

        if not isinstance(scene.get("sounds", []), list):
            raise ValueError(f"Scene {number} sounds must be a list.")

    return True
