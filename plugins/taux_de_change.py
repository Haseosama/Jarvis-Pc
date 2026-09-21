"""Ported from Jarvis-Android: plugins/taux_de_change.json (http)."""
from plugins._android_runtime import run_http

PLUGIN = {
    "name": "taux_de_change",
    "description": "Donne le taux de change du jour entre deux devises (source : Banque centrale européenne). Pour « combien font 50 euros en dollars ».",
    "parameters": {
        "type": "OBJECT",
        "properties": {
            "base": {
                "type": "STRING",
                "description": "Devise de départ, code en majuscules : EUR, USD, GBP…"
            },
            "cible": {
                "type": "STRING",
                "description": "Devise d'arrivée, code en majuscules"
            }
        },
        "required": [
            "base",
            "cible"
        ]
    }
}


def run(parameters: dict, player=None, session_memory=None) -> str:
    result = run_http(PLUGIN, 'https://api.frankfurter.dev/v1/latest?base={base}&symbols={cible}', parameters)
    if player:
        try:
            player.write_log(f"JARVIS: {result[:200]}")
        except Exception:
            pass
    return result
