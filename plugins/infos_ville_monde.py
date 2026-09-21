"""Ported from Jarvis-Android: plugins/infos_ville_monde.json (http)."""
from plugins._android_runtime import run_http

PLUGIN = {
    "name": "infos_ville_monde",
    "description": "Donne les informations d'une ville du monde : pays, latitude, longitude, altitude, fuseau horaire et population (source : Open-Meteo). Pour « où est… », « quel fuseau horaire à… », « combien d'habitants à… ».",
    "parameters": {
        "type": "OBJECT",
        "properties": {
            "ville": {
                "type": "STRING",
                "description": "Nom de la ville"
            }
        },
        "required": [
            "ville"
        ]
    }
}


def run(parameters: dict, player=None, session_memory=None) -> str:
    result = run_http(PLUGIN, 'https://geocoding-api.open-meteo.com/v1/search?name={ville}&count=1&language=fr', parameters)
    if player:
        try:
            player.write_log(f"JARVIS: {result[:200]}")
        except Exception:
            pass
    return result
