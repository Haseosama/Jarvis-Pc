"""Ported from Jarvis-Android: plugins/recette.json (open)."""
from plugins._android_runtime import run_open

PLUGIN = {
    "name": "recette",
    "description": "Ouvre une recherche de recettes de cuisine sur Marmiton. Pour « une idée de recette avec… ».",
    "parameters": {
        "type": "OBJECT",
        "properties": {
            "plat": {
                "type": "STRING",
                "description": "Le plat ou les ingrédients"
            }
        },
        "required": [
            "plat"
        ]
    }
}


def run(parameters: dict, player=None, session_memory=None) -> str:
    result = run_open(PLUGIN, 'https://www.marmiton.org/recettes/recherche.aspx?aqt={plat}', parameters)
    if player:
        try:
            player.write_log(f"JARVIS: {result[:200]}")
        except Exception:
            pass
    return result
