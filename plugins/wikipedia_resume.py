"""Ported from Jarvis-Android: plugins/wikipedia_resume.json (http)."""
from plugins._android_runtime import run_http

PLUGIN = {
    "name": "wikipedia_resume",
    "description": "Donne le résumé d'un sujet sur Wikipédia en français (personne, lieu, notion). Pour « c'est quoi… », « qui est… ».",
    "parameters": {
        "type": "OBJECT",
        "properties": {
            "sujet": {
                "type": "STRING",
                "description": "Titre de l'article Wikipédia, par exemple Tour Eiffel"
            }
        },
        "required": [
            "sujet"
        ]
    }
}


def run(parameters: dict, player=None, session_memory=None) -> str:
    result = run_http(PLUGIN, 'https://fr.wikipedia.org/api/rest_v1/page/summary/{sujet}', parameters, 'extract')
    if player:
        try:
            player.write_log(f"JARVIS: {result[:200]}")
        except Exception:
            pass
    return result
