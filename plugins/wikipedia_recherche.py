"""Ported from Jarvis-Android: plugins/wikipedia_recherche.json (http)."""
from plugins._android_runtime import run_http

PLUGIN = {
    "name": "wikipedia_recherche",
    "description": "Cherche des articles de Wikipédia en français sur un sujet et donne les titres et les liens (source : Wikipédia). Pour « trouve un article sur… ».",
    "parameters": {
        "type": "OBJECT",
        "properties": {
            "sujet": {
                "type": "STRING",
                "description": "Le sujet"
            }
        },
        "required": [
            "sujet"
        ]
    }
}


def run(parameters: dict, player=None, session_memory=None) -> str:
    result = run_http(PLUGIN, 'https://fr.wikipedia.org/w/api.php?action=opensearch&search={sujet}&limit=5&format=json', parameters)
    if player:
        try:
            player.write_log(f"JARVIS: {result[:200]}")
        except Exception:
            pass
    return result
