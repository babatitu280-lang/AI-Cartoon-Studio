# AI Cartoon Studio
# Detailed sound design and synchronisation foundation

from dataclasses import dataclass, field


@dataclass
class AudioCue:
    filename: str
    start: float
    volume: float = 1.0
    category: str = "sfx"
    duration: float = 0.0


@dataclass
class ActionSoundMap:
    action: str
    sounds: list = field(default_factory=list)


# Detailed action-to-sound mapping
ACTION_SOUNDS = {
    "walk": [
        "tiny_footsteps",
        "surface_contact"
    ],
    "run": [
        "fast_footsteps",
        "rapid_movement"
    ],
    "eat": [
        "bite",
        "crunch",
        "chewing",
        "swallow"
    ],
    "jump": [
        "takeoff",
        "whoosh",
        "landing"
    ],
    "fall": [
        "falling_whoosh",
        "impact",
        "bounce"
    ],
    "sneak": [
        "soft_footsteps",
        "clothing_movement"
    ],
    "react": [
        "gasp",
        "squeak",
        "grunt"
    ],
    "object_interaction": [
        "touch",
        "tap",
        "rattle",
        "creak"
    ],
    "vacuum": [
        "motor",
        "air_suction",
        "airflow"
    ]
}


SOUND_CATEGORIES = [
    "footsteps",
    "eating",
    "character_vocalisations",
    "impacts",
    "whooshes",
    "environment",
    "object_interaction",
    "vacuum",
    "music",
    "silence"
]


def get_action_sounds(action):
    return ACTION_SOUNDS.get(action, [])


def validate_audio(cues, episode_duration):
    for cue in cues:
        if cue.start < 0:
            raise ValueError("Sound cannot start before the episode.")

        if cue.start >= episode_duration:
            raise ValueError("Sound starts outside the episode.")

        if not 0 <= cue.volume <= 1:
            raise ValueError("Volume must be between 0 and 1.")

        if cue.duration < 0:
            raise ValueError("Sound duration cannot be negative.")

    return True
