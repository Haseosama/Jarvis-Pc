"""Ported from Jarvis-Android: plugins/traduction_texte.json (http)."""
from plugins._android_runtime import run_http

PLUGIN = {
    "name": "traduction_texte",
    "description": "Traduit un texte et donne directement la traduction (source : MyMemory, sans clé, quota quotidien). Pour « comment dit-on … en anglais », « traduis cette phrase en espagnol ».",
    "parameters": {
        "type": "OBJECT",
        "properties": {
            "texte": {
                "type": "STRING",
                "description": "Le texte à traduire"
            },
            "langues": {
                "type": "STRING",
                "description": "Langue source puis langue cible séparées par | , par exemple fr|en, fr|es, en|fr, fr|de"
            }
        },
        "required": [
            "texte",
            "langues"
        ]
    }
}


def run(parameters: dict, player=None, session_memory=None) -> str:
    result = run_http(PLUGIN, 'https://api.mymemory.translated.net/get?q={texte}&langpair={langues}', parameters, 'responseData.translatedText')
    if player:
        try:
            player.write_log(f"JARVIS: {result[:200]}")
        except Exception:
            pass
    return result
