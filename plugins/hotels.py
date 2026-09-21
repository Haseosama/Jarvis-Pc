"""Ported from Jarvis-Android: plugins/hotels.json (open)."""
from plugins._android_runtime import run_open

PLUGIN = {
    "name": "hotels",
    "description": "Ouvre Google Hôtels sur une ville. Pour « un hôtel à Nantes », « où dormir à Rome ».",
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
    result = run_open(PLUGIN, 'https://www.google.com/travel/hotels/{ville}', parameters)
    if player:
        try:
            player.write_log(f"JARVIS: {result[:200]}")
        except Exception:
            pass
    return result
