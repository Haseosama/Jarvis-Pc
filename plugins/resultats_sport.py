"""Ported from Jarvis-Android: plugins/resultats_sport.json (open)."""
from plugins._android_runtime import run_open

PLUGIN = {
    "name": "resultats_sport",
    "description": "Ouvre les résultats sportifs récents d'une équipe ou d'un joueur dans Google. Pour « quel est le score de… », « qui a gagné hier ».",
    "parameters": {
        "type": "OBJECT",
        "properties": {
            "equipe": {
                "type": "STRING",
                "description": "Équipe, joueur ou compétition"
            }
        },
        "required": [
            "equipe"
        ]
    }
}


def run(parameters: dict, player=None, session_memory=None) -> str:
    result = run_open(PLUGIN, 'https://www.google.com/search?q=score+{equipe}', parameters)
    if player:
        try:
            player.write_log(f"JARVIS: {result[:200]}")
        except Exception:
            pass
    return result
