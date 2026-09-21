"""Ported from Jarvis-Android: plugins/cocktail_hasard.json (http)."""
from plugins._android_runtime import run_http

PLUGIN = {
    "name": "cocktail_hasard",
    "description": "Propose un cocktail au hasard : nom, catégorie, verre et préparation, en anglais (source : thecocktaildb.com). Pour « un cocktail pour ce soir ».",
    "parameters": {
        "type": "OBJECT",
        "properties": {},
        "required": []
    }
}


def run(parameters: dict, player=None, session_memory=None) -> str:
    result = run_http(PLUGIN, 'https://www.thecocktaildb.com/api/json/v1/1/random.php', parameters)
    if player:
        try:
            player.write_log(f"JARVIS: {result[:200]}")
        except Exception:
            pass
    return result
