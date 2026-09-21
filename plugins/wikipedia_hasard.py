"""Ported from Jarvis-Android: plugins/wikipedia_hasard.json (http)."""
from plugins._android_runtime import run_http

PLUGIN = {
    "name": "wikipedia_hasard",
    "description": "Lit le résumé d'un article de Wikipédia en français tiré au hasard. Pour « apprends-moi quelque chose », « raconte-moi un truc au hasard ».",
    "parameters": {
        "type": "OBJECT",
        "properties": {},
        "required": []
    }
}


def run(parameters: dict, player=None, session_memory=None) -> str:
    result = run_http(PLUGIN, 'https://fr.wikipedia.org/api/rest_v1/page/random/summary', parameters, 'extract')
    if player:
        try:
            player.write_log(f"JARVIS: {result[:200]}")
        except Exception:
            pass
    return result
