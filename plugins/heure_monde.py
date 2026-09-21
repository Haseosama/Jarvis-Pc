"""Ported from Jarvis-Android: plugins/heure_monde.json (http)."""
from plugins._android_runtime import run_http

PLUGIN = {
    "name": "heure_monde",
    "description": "Donne l'heure actuelle dans un fuseau horaire (source : timeapi.io). Pour « quelle heure est-il à Tokyo ».",
    "parameters": {
        "type": "OBJECT",
        "properties": {
            "fuseau": {
                "type": "STRING",
                "description": "Fuseau IANA, par exemple Asia/Tokyo, America/New_York, Europe/Paris"
            }
        },
        "required": [
            "fuseau"
        ]
    }
}


def run(parameters: dict, player=None, session_memory=None) -> str:
    result = run_http(PLUGIN, 'https://timeapi.io/api/time/current/zone?timeZone={fuseau}', parameters, 'dateTime')
    if player:
        try:
            player.write_log(f"JARVIS: {result[:200]}")
        except Exception:
            pass
    return result
