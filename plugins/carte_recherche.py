"""Ported from Jarvis-Android: plugins/carte_recherche.json (open)."""
from plugins._android_runtime import run_open

PLUGIN = {
    "name": "carte_recherche",
    "description": "Ouvre Google Maps sur une recherche de lieu, par exemple une pharmacie, un restaurant ou une station-service.",
    "parameters": {
        "type": "OBJECT",
        "properties": {
            "lieu": {
                "type": "STRING",
                "description": "Ce qu'il faut chercher"
            }
        },
        "required": [
            "lieu"
        ]
    }
}


def run(parameters: dict, player=None, session_memory=None) -> str:
    result = run_open(PLUGIN, 'https://www.google.com/maps/search/{lieu}', parameters)
    if player:
        try:
            player.write_log(f"JARVIS: {result[:200]}")
        except Exception:
            pass
    return result
