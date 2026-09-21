"""Ported from Jarvis-Android: plugins/cinema_seances.json (open)."""
from plugins._android_runtime import run_open

PLUGIN = {
    "name": "cinema_seances",
    "description": "Ouvre les séances de cinéma d'une ville dans Google. Pour « qu'est-ce qui passe au cinéma », « des séances ce soir ».",
    "parameters": {
        "type": "OBJECT",
        "properties": {
            "ville": {
                "type": "STRING",
                "description": "Ville"
            }
        },
        "required": [
            "ville"
        ]
    }
}


def run(parameters: dict, player=None, session_memory=None) -> str:
    result = run_open(PLUGIN, 'https://www.google.com/search?q=séances+cinéma+{ville}', parameters)
    if player:
        try:
            player.write_log(f"JARVIS: {result[:200]}")
        except Exception:
            pass
    return result
