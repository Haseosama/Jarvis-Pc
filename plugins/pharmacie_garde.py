"""Ported from Jarvis-Android: plugins/pharmacie_garde.json (open)."""
from plugins._android_runtime import run_open

PLUGIN = {
    "name": "pharmacie_garde",
    "description": "Ouvre Google Maps sur les pharmacies de garde près d'un lieu. Pour « une pharmacie de garde », « pharmacie ouverte cette nuit ».",
    "parameters": {
        "type": "OBJECT",
        "properties": {
            "lieu": {
                "type": "STRING",
                "description": "Ville ou quartier (facultatif : sinon autour de la position)"
            }
        },
        "required": []
    }
}


def run(parameters: dict, player=None, session_memory=None) -> str:
    result = run_open(PLUGIN, 'https://www.google.com/maps/search/pharmacie+de+garde+{lieu}', parameters)
    if player:
        try:
            player.write_log(f"JARVIS: {result[:200]}")
        except Exception:
            pass
    return result
