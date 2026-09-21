"""Ported from Jarvis-Android: plugins/jours_feries.json (http)."""
from plugins._android_runtime import run_http

PLUGIN = {
    "name": "jours_feries",
    "description": "Donne les prochains jours fériés d'un pays. Pour « c'est quand le prochain jour férié ».",
    "parameters": {
        "type": "OBJECT",
        "properties": {
            "pays": {
                "type": "STRING",
                "description": "Code pays à 2 lettres en majuscules : FR, BE, CH, CA…"
            }
        },
        "required": [
            "pays"
        ]
    }
}


def run(parameters: dict, player=None, session_memory=None) -> str:
    result = run_http(PLUGIN, 'https://date.nager.at/api/v3/NextPublicHolidays/{pays}', parameters)
    if player:
        try:
            player.write_log(f"JARVIS: {result[:200]}")
        except Exception:
            pass
    return result
