"""Ported from Jarvis-Android: plugins/gps_adresse.json (http)."""
from plugins._android_runtime import run_http

PLUGIN = {
    "name": "gps_adresse",
    "description": "Donne les coordonnées GPS d'une adresse postale ou d'une commune en France : longitude puis latitude (source : adresse.data.gouv.fr). Les monuments ne sont pas toujours reconnus : donner une adresse. Pour « quelles sont les coordonnées de… ».",
    "parameters": {
        "type": "OBJECT",
        "properties": {
            "recherche": {
                "type": "STRING",
                "description": "Adresse postale ou commune"
            }
        },
        "required": [
            "recherche"
        ]
    }
}


def run(parameters: dict, player=None, session_memory=None) -> str:
    result = run_http(PLUGIN, 'https://api-adresse.data.gouv.fr/search/?q={recherche}&limit=1', parameters, 'features.0.geometry.coordinates')
    if player:
        try:
            player.write_log(f"JARVIS: {result[:200]}")
        except Exception:
            pass
    return result
