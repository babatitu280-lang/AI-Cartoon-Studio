PROJECT_NAME = "AI Cartoon Studio"

VIDEO = {
    "width": 1920,
    "height": 1080,
    "fps": 24,
    "format": "mp4",
    "codec": "libx264"
}

EPISODE = {
    "minimum_duration": 180,
    "maximum_duration": 300,
    "dialogue": False
}

VISUALS = {
    "character_style": "polished_2d",
    "environment_style": "3d",
    "environment_engine": "blender",
    "character_rendering": "transparent_2d_assets",
    "compositing": True,
    "reusable_character_assets": True,
    "reusable_3d_environments": True
}

AUDIO = {
    "sound_effects": True,
    "character_vocalisations": True,
    "background_music": True,
    "synchronised_to_actions": True,
    "dialogue": False
}

CHARACTER_NAMES = ["bobo", "rexy"]
