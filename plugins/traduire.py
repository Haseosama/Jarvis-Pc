"""Ported from Jarvis-Android: plugins/traduire.json (open)."""
from plugins._android_runtime import run_open

PLUGIN = {
    "name": "traduire",
    "description": "Ouvre Google Traduction avec un texte et la langue cible. Pour « traduis … en anglais ».",
    "parameters": {
        "type": "OBJECT",
        "properties": {
            "texte": {
                "type": "STRING",
                "description": "Le texte à traduire"
            },
            "langue": {
                "type": "STRING",
                "description": "Code de la langue cible : en, fr, es, tl (tagalog), de…"
            }
        },
        "required": [
            "texte",
            "langue"
        ]
    }
}


def run(parameters: dict, player=None, session_memory=None) -> str:
    result = run_open(PLUGIN, 'https://translate.google.com/?sl=auto&tl={langue}&text={texte}&op=translate', parameters)
    if player:
        try:
            player.write_log(f"JARVIS: {result[:200]}")
        except Exception:
            pass
    return result
