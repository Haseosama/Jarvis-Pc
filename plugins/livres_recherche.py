"""Ported from Jarvis-Android: plugins/livres_recherche.json (open)."""
from plugins._android_runtime import run_open

PLUGIN = {
    "name": "livres_recherche",
    "description": "Ouvre Google Livres sur un titre, un auteur ou un sujet. Pour « trouve-moi ce livre », « des livres sur… ».",
    "parameters": {
        "type": "OBJECT",
        "properties": {
            "titre": {
                "type": "STRING",
                "description": "Titre, auteur ou sujet"
            }
        },
        "required": [
            "titre"
        ]
    }
}


def run(parameters: dict, player=None, session_memory=None) -> str:
    result = run_open(PLUGIN, 'https://www.google.com/search?tbm=bks&q={titre}', parameters)
    if player:
        try:
            player.write_log(f"JARVIS: {result[:200]}")
        except Exception:
            pass
    return result
