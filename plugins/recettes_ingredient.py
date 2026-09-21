"""Ported from Jarvis-Android: plugins/recettes_ingredient.json (http)."""
from plugins._android_runtime import run_http

PLUGIN = {
    "name": "recettes_ingredient",
    "description": "Liste des plats qui utilisent un ingrédient (noms et pays d'origine, en anglais, source : themealdb.com). Pour « que faire avec du poulet », « des idées avec des œufs ».",
    "parameters": {
        "type": "OBJECT",
        "properties": {
            "ingredient": {
                "type": "STRING",
                "description": "Ingrédient en anglais, par exemple chicken, beef, salmon, eggs, rice"
            }
        },
        "required": [
            "ingredient"
        ]
    }
}


def run(parameters: dict, player=None, session_memory=None) -> str:
    result = run_http(PLUGIN, 'https://www.themealdb.com/api/json/v1/1/filter.php?i={ingredient}', parameters)
    if player:
        try:
            player.write_log(f"JARVIS: {result[:200]}")
        except Exception:
            pass
    return result
