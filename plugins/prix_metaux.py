"""Ported from Jarvis-Android: plugins/prix_metaux.json (http)."""
from plugins._android_runtime import run_http

PLUGIN = {
    "name": "prix_metaux",
    "description": "Donne le cours d'un métal précieux en dollars américains l'once troy (source : gold-api.com). Pour « combien vaut l'or », « le cours de l'argent ».",
    "parameters": {
        "type": "OBJECT",
        "properties": {
            "metal": {
                "type": "STRING",
                "description": "XAU pour l'or, XAG pour l'argent, XPT pour le platine, XPD pour le palladium"
            }
        },
        "required": [
            "metal"
        ]
    }
}


def run(parameters: dict, player=None, session_memory=None) -> str:
    result = run_http(PLUGIN, 'https://api.gold-api.com/price/{metal}', parameters, 'price')
    if player:
        try:
            player.write_log(f"JARVIS: {result[:200]}")
        except Exception:
            pass
    return result
