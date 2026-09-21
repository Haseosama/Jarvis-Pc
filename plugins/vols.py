"""Ported from Jarvis-Android: plugins/vols.json (open)."""
from plugins._android_runtime import run_open

PLUGIN = {
    "name": "vols",
    "description": "Ouvre Google Flights sur des vols entre deux villes. Pour « des vols pour Lisbonne », « un billet d'avion Paris New York ».",
    "parameters": {
        "type": "OBJECT",
        "properties": {
            "depart": {
                "type": "STRING",
                "description": "Ville ou aéroport de départ"
            },
            "arrivee": {
                "type": "STRING",
                "description": "Ville ou aéroport d'arrivée"
            }
        },
        "required": [
            "depart",
            "arrivee"
        ]
    }
}


def run(parameters: dict, player=None, session_memory=None) -> str:
    result = run_open(PLUGIN, 'https://www.google.com/travel/flights?q=vols+de+{depart}+a+{arrivee}', parameters)
    if player:
        try:
            player.write_log(f"JARVIS: {result[:200]}")
        except Exception:
            pass
    return result
