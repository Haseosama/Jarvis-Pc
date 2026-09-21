"""Ported from Jarvis-Android: plugins/comparer_prix.json (open)."""
from plugins._android_runtime import run_open

PLUGIN = {
    "name": "comparer_prix",
    "description": "Ouvre Google Shopping pour comparer les prix d'un produit. Pour « le meilleur prix pour… », « où acheter… ».",
    "parameters": {
        "type": "OBJECT",
        "properties": {
            "produit": {
                "type": "STRING",
                "description": "Le produit"
            }
        },
        "required": [
            "produit"
        ]
    }
}


def run(parameters: dict, player=None, session_memory=None) -> str:
    result = run_open(PLUGIN, 'https://www.google.com/search?tbm=shop&q={produit}', parameters)
    if player:
        try:
            player.write_log(f"JARVIS: {result[:200]}")
        except Exception:
            pass
    return result
