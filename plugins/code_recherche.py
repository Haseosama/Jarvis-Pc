"""Ported from Jarvis-Android: plugins/code_recherche.json (open)."""
from plugins._android_runtime import run_open

PLUGIN = {
    "name": "code_recherche",
    "description": "Ouvre Stack Overflow sur une question de programmation. Pour « comment faire … en Kotlin », « cette erreur ».",
    "parameters": {
        "type": "OBJECT",
        "properties": {
            "question": {
                "type": "STRING",
                "description": "La question ou le message d'erreur"
            }
        },
        "required": [
            "question"
        ]
    }
}


def run(parameters: dict, player=None, session_memory=None) -> str:
    result = run_open(PLUGIN, 'https://stackoverflow.com/search?q={question}', parameters)
    if player:
        try:
            player.write_log(f"JARVIS: {result[:200]}")
        except Exception:
            pass
    return result
