"""Ported from Jarvis-Android: plugins/youtube_recherche.json (open)."""
from plugins._android_runtime import run_open

PLUGIN = {
    "name": "youtube_recherche",
    "description": "Ouvre la page de résultats YouTube pour une recherche (musique, tutoriel, vidéo).",
    "parameters": {
        "type": "OBJECT",
        "properties": {
            "requete": {
                "type": "STRING",
                "description": "Ce qu'il faut chercher sur YouTube"
            }
        },
        "required": [
            "requete"
        ]
    }
}


def run(parameters: dict, player=None, session_memory=None) -> str:
    result = run_open(PLUGIN, 'https://www.youtube.com/results?search_query={requete}', parameters)
    if player:
        try:
            player.write_log(f"JARVIS: {result[:200]}")
        except Exception:
            pass
    return result
