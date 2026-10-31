# AI Cartoon Studio
# Permanent character specifications

CHARACTERS = {
    "bobo": {
        "name": "Bobo",
        "species": "Dinosaur",
        "body_color": "#F4B52E",
        "belly_color": "#F7D58A",
        "spike_color": "#79502E",
        "body_type": "chubby",
        "belly": "large",
        "feet": "tiny",
        "personality": [
            "food-loving",
            "lazy",
            "goofy"
        ]
    },

    "rexy": {
        "name": "Rexy",
        "species": "Dinosaur",
        "body_color": "#9655C9",
        "belly_color": "#C99AE8",
        "spike_color": "#60358C",
        "body_type": "thin",
        "tail": "long",
        "limbs": "long",
        "personality": [
            "energetic",
            "clever",
            "mischievous"
        ]
    }
}

def get_character(name):
    return CHARACTERS[name.lower()]
