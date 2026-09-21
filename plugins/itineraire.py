"""Ported from Jarvis-Android: plugins/itineraire.json (open)."""
from plugins._android_runtime import run_open

PLUGIN = {
    "name": "itineraire",
    "description": "Ouvre Google Maps avec l'itinéraire vers une destination depuis la position actuelle. Pour « emmène-moi à… ».",
    "parameters": {
        "type": "OBJECT",
        "properties": {
            "destination": {
                "type": "STRING",
                "description": "Adresse ou nom du lieu"
            },
            "mode": {
                "type": "STRING",
                "description": "driving, walking, bicycling ou transit (driving par défaut)"
            }
        },
        "required": [
            "destination"
        ]
    }
}


def run(parameters: dict, player=None, session_memory=None) -> str:
    result = run_open(PLUGIN, 'https://www.google.com/maps/dir/?api=1&destination={destination}&travelmode={mode}', parameters)
    if player:
        try:
            player.write_log(f"JARVIS: {result[:200]}")
        except Exception:
            pass
    return result
