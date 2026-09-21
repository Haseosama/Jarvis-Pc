"""Ported from Jarvis-Android: plugins/livre_infos.json (http)."""
from plugins._android_runtime import run_http

PLUGIN = {
    "name": "livre_infos",
    "description": "Cherche un livre et donne jusqu'à 3 résultats avec auteur et année de première publication (source : Open Library). Pour « qui a écrit… », « en quelle année est sorti… ».",
    "parameters": {
        "type": "OBJECT",
        "properties": {
            "titre": {
                "type": "STRING",
                "description": "Titre ou mots du titre"
            }
        },
        "required": [
            "titre"
        ]
    }
}


def run(parameters: dict, player=None, session_memory=None) -> str:
    result = run_http(PLUGIN, 'https://openlibrary.org/search.json?q={titre}&limit=3&fields=title,author_name,first_publish_year', parameters)
    if player:
        try:
            player.write_log(f"JARVIS: {result[:200]}")
        except Exception:
            pass
    return result
