# AI Cartoon Studio
# Basic system verification

from studio.characters import CHARACTERS, get_character
from studio.animation import animate_position, bounce
from studio.audio import get_action_sounds
from studio.timeline import Scene, Action, SoundCue, validate_episode
from studio.scenes import create_scene, add_action, add_sound


def run_checks():
    # Check character specifications
    assert get_character("bobo") == CHARACTERS["bobo"]
    assert get_character("rexy") == CHARACTERS["rexy"]

    # Check animation calculations
    position = animate_position((0, 0), (100, 100), 0.5)
    assert position == (50, 50)

    assert bounce(0.5) >= 0

    # Check detailed sound mapping
    assert "chewing" in get_action_sounds("eat")
    assert "tiny_footsteps" in get_action_sounds("walk")

    # Check scene creation and timing
    scene = create_scene("Test scene", 5, "test_background")

    add_action(scene, "bobo", "walk", 0, 2)
    add_sound(scene, "footsteps.wav", 0.5)

    test_episode = [
        Scene(
            name=scene.name,
            duration=scene.duration,
            actions=scene.actions,
            sounds=[
                SoundCue(
                    sound=sound.sound,
                    start=sound.start,
                )
                for sound in scene.sounds
            ],
        )
    ]

    assert validate_episode(test_episode)

    return "All basic system checks passed!"


if __name__ == "__main__":
    print(run_checks())
