"""Ported from Jarvis-Android: plugins/fait_insolite.json (http)."""
from plugins._android_runtime import run_http

PLUGIN = {
    "name": "fait_insolite",
    "description": "Donne un fait insolite au hasard, en anglais (source : uselessfacts.jsph.pl). Pour « raconte-moi un fait amusant », « le saviez-vous ».",
    "parameters": {
        "type": "OBJECT",
        "properties": {},
        "required": []
    }
}


def run(parameters: dict, player=None, session_memory=None) -> str:
    result = run_http(PLUGIN, 'https://uselessfacts.jsph.pl/api/v2/facts/random?language=en', parameters, 'text')
    if player:
        try:
            player.write_log(f"JARVIS: {result[:200]}")
        except Exception:
            pass
    return result
