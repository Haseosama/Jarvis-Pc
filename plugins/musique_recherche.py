"""Ported from Jarvis-Android: plugins/musique_recherche.json (open)."""
from plugins._android_runtime import run_open

PLUGIN = {
    "name": "musique_recherche",
    "description": "Ouvre Spotify sur une recherche de morceau, d'artiste ou de playlist. Pour « mets du jazz », « joue Daft Punk ».",
    "parameters": {
        "type": "OBJECT",
        "properties": {
            "recherche": {
                "type": "STRING",
                "description": "Morceau, artiste ou style"
            }
        },
        "required": [
            "recherche"
        ]
    }
}


def run(parameters: dict, player=None, session_memory=None) -> str:
    result = run_open(PLUGIN, 'https://open.spotify.com/search/{recherche}', parameters)
    if player:
        try:
            player.write_log(f"JARVIS: {result[:200]}")
        except Exception:
            pass
    return result
