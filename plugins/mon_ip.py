"""Ported from Jarvis-Android: plugins/mon_ip.json (http)."""
from plugins._android_runtime import run_http

PLUGIN = {
    "name": "mon_ip",
    "description": "Donne l'adresse IP publique du téléphone (celle que voient les sites web), source : ipify.org. Pour « quelle est mon adresse IP ».",
    "parameters": {
        "type": "OBJECT",
        "properties": {},
        "required": []
    }
}


def run(parameters: dict, player=None, session_memory=None) -> str:
    result = run_http(PLUGIN, 'https://api.ipify.org?format=json', parameters, 'ip')
    if player:
        try:
            player.write_log(f"JARVIS: {result[:200]}")
        except Exception:
            pass
    return result
