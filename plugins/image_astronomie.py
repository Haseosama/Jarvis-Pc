"""Ported from Jarvis-Android: plugins/image_astronomie.json (http)."""
from plugins._android_runtime import run_http

PLUGIN = {
    "name": "image_astronomie",
    "description": "Lit l'explication de l'image astronomique du jour de la NASA (en anglais : à traduire et résumer). Pour « quelle est l'image de l'espace du jour ».",
    "parameters": {
        "type": "OBJECT",
        "properties": {},
        "required": []
    }
}


def run(parameters: dict, player=None, session_memory=None) -> str:
    result = run_http(PLUGIN, 'https://api.nasa.gov/planetary/apod?api_key=DEMO_KEY', parameters, 'explanation')
    if player:
        try:
            player.write_log(f"JARVIS: {result[:200]}")
        except Exception:
            pass
    return result
