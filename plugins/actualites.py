"""Ported from Jarvis-Android: plugins/actualites.json (open)."""
from plugins._android_runtime import run_open

PLUGIN = {
    "name": "actualites",
    "description": "Ouvre Google Actualités sur un sujet. Pour « quoi de neuf sur… », « les infos sur… ».",
    "parameters": {
        "type": "OBJECT",
        "properties": {
            "sujet": {
                "type": "STRING",
                "description": "Le sujet d'actualité"
            }
        },
        "required": [
            "sujet"
        ]
    }
}


def run(parameters: dict, player=None, session_memory=None) -> str:
    result = run_open(PLUGIN, 'https://news.google.com/search?q={sujet}&hl=fr&gl=FR&ceid=FR:fr', parameters)
    if player:
        try:
            player.write_log(f"JARVIS: {result[:200]}")
        except Exception:
            pass
    return result
