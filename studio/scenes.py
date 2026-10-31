# AI Cartoon Studio
# Episode scene management

from dataclasses import dataclass, field

from studio.timeline import (
    Action,
    SoundCue,
    validate_scene
)


@dataclass
class CartoonScene:
    name: str
    duration: float
    background: str
    actions: list = field(default_factory=list)
    sounds: list = field(default_factory=list)


def create_scene(name, duration, background):
    return CartoonScene(
        name=name,
        duration=duration,
        background=background
    )


def add_action(scene, character, movement, start, duration):
    action = Action(
        character=character,
        movement=movement,
        start=start,
        duration=duration
    )

    scene.actions.append(action)
    return action


def add_sound(scene, filename, start, volume=1.0):
    sound = SoundCue(
        sound=filename,
        start=start,
        volume=volume
    )

    scene.sounds.append(sound)
    return sound


def validate_cartoon_scene(scene):
    return validate_scene(scene)
