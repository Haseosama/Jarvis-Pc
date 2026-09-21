"""Ported from Jarvis-Android: plugins/idee_repas.json (http)."""
from plugins._android_runtime import run_http

PLUGIN = {
    "name": "idee_repas",
    "description": "Propose un plat au hasard : nom, catégorie, pays d'origine et début de la recette, en anglais (source : themealdb.com). Pour « qu'est-ce que je mange ce soir ? ».",
    "parameters": {
        "type": "OBJECT",
        "properties": {},
        "required": []
    }
}


def run(parameters: dict, player=None, session_memory=None) -> str:
    result = run_http(PLUGIN, 'https://www.themealdb.com/api/json/v1/1/random.php', parameters)
    if player:
        try:
            player.write_log(f"JARVIS: {result[:200]}")
        except Exception:
            pass
    return result
