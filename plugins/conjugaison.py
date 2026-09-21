"""Ported from Jarvis-Android: plugins/conjugaison.json (open)."""
from plugins._android_runtime import run_open

PLUGIN = {
    "name": "conjugaison",
    "description": "Ouvre la conjugaison complète d'un verbe (Le Conjugueur). Pour « conjugue le verbe… ».",
    "parameters": {
        "type": "OBJECT",
        "properties": {
            "verbe": {
                "type": "STRING",
                "description": "Le verbe à l'infinitif, sans espace"
            }
        },
        "required": [
            "verbe"
        ]
    }
}


def run(parameters: dict, player=None, session_memory=None) -> str:
    result = run_open(PLUGIN, 'https://leconjugueur.lefigaro.fr/conjugaison/verbe/{verbe}.html', parameters)
    if player:
        try:
            player.write_log(f"JARVIS: {result[:200]}")
        except Exception:
            pass
    return result
