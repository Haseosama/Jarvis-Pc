"""Ported from Jarvis-Android: plugins/citation.json (http)."""
from plugins._android_runtime import run_http

PLUGIN = {
    "name": "citation",
    "description": "Donne une citation au hasard avec son auteur, en anglais (source : zenquotes.io). Pour « une citation », « motive-moi ».",
    "parameters": {
        "type": "OBJECT",
        "properties": {},
        "required": []
    }
}


def run(parameters: dict, player=None, session_memory=None) -> str:
    result = run_http(PLUGIN, 'https://zenquotes.io/api/random', parameters)
    if player:
        try:
            player.write_log(f"JARVIS: {result[:200]}")
        except Exception:
            pass
    return result
