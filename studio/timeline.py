# AI Cartoon Studio
# Scene timing and sound synchronisation system

from dataclasses import dataclass, field


@dataclass
class Action:
    character: str
    movement: str
    start: float
    duration: float


@dataclass
class SoundCue:
    sound: str
    start: float
    volume: float = 1.0


@dataclass
class Scene:
    name: str
    duration: float
    actions: list = field(default_factory=list)
    sounds: list = field(default_factory=list)


def validate_scene(scene):
    if scene.duration <= 0:
        raise ValueError("Scene duration must be positive.")

    for action in scene.actions:
        if action.start < 0 or action.duration <= 0:
            raise ValueError("Invalid action timing.")

        if action.start + action.duration > scene.duration:
            raise ValueError("Action exceeds scene duration.")

    for sound in scene.sounds:
        if sound.start < 0 or sound.start > scene.duration:
            raise ValueError("Invalid sound timing.")

    return True


def get_total_duration(scenes):
    return sum(scene.duration for scene in scenes)


def validate_episode(scenes):
    if not scenes:
        raise ValueError("Episode has no scenes.")

    for scene in scenes:
        validate_scene(scene)

    return True
