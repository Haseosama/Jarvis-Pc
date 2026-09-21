"""Ported from Jarvis-Android: plugins/legifrance.json (open)."""
from plugins._android_runtime import run_open

PLUGIN = {
    "name": "legifrance",
    "description": "Ouvre la recherche de Légifrance sur un texte de loi ou un sujet juridique. Pour « que dit la loi sur… ».",
    "parameters": {
        "type": "OBJECT",
        "properties": {
            "recherche": {
                "type": "STRING",
                "description": "Le sujet ou l'article"
            }
        },
        "required": [
            "recherche"
        ]
    }
}


def run(parameters: dict, player=None, session_memory=None) -> str:
    result = run_open(PLUGIN, 'https://www.legifrance.gouv.fr/search/all?tab_selection=all&searchField=ALL&query={recherche}', parameters)
    if player:
        try:
            player.write_log(f"JARVIS: {result[:200]}")
        except Exception:
            pass
    return result
