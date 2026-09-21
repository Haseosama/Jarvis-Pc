"""Ported from Jarvis-Android: plugins/pages_jaunes.json (open)."""
from plugins._android_runtime import run_open

PLUGIN = {
    "name": "pages_jaunes",
    "description": "Ouvre les Pages Jaunes sur un professionnel ou un commerce près d'un lieu. Pour « un plombier à… », « un serrurier près de chez moi ».",
    "parameters": {
        "type": "OBJECT",
        "properties": {
            "quoi": {
                "type": "STRING",
                "description": "Le métier ou le commerce"
            },
            "ou": {
                "type": "STRING",
                "description": "La ville"
            }
        },
        "required": [
            "quoi",
            "ou"
        ]
    }
}


def run(parameters: dict, player=None, session_memory=None) -> str:
    result = run_open(PLUGIN, 'https://www.pagesjaunes.fr/annuaire/chercherlespros?quoiqui={quoi}&ou={ou}', parameters)
    if player:
        try:
            player.write_log(f"JARVIS: {result[:200]}")
        except Exception:
            pass
    return result
