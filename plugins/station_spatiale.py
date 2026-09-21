"""Ported from Jarvis-Android: plugins/station_spatiale.json (http)."""
from plugins._android_runtime import run_http

PLUGIN = {
    "name": "station_spatiale",
    "description": "Donne la position actuelle de la Station spatiale internationale : latitude, longitude, altitude en km, vitesse en km/h, et si elle est éclairée par le soleil ou dans l'ombre (source : wheretheiss.at). Pour « où est l'ISS ? ».",
    "parameters": {
        "type": "OBJECT",
        "properties": {},
        "required": []
    }
}


def run(parameters: dict, player=None, session_memory=None) -> str:
    result = run_http(PLUGIN, 'https://api.wheretheiss.at/v1/satellites/25544', parameters)
    if player:
        try:
            player.write_log(f"JARVIS: {result[:200]}")
        except Exception:
            pass
    return result
