"""Ported from Jarvis-Android: plugins/asteroides_du_jour.json (http)."""
from plugins._android_runtime import run_http

PLUGIN = {
    "name": "asteroides_du_jour",
    "description": "Donne le nombre d'astéroïdes qui passent près de la Terre aujourd'hui (source : NASA NeoWs, clé de démonstration limitée). Pour « y a-t-il des astéroïdes aujourd'hui ».",
    "parameters": {
        "type": "OBJECT",
        "properties": {},
        "required": []
    }
}


def run(parameters: dict, player=None, session_memory=None) -> str:
    result = run_http(PLUGIN, 'https://api.nasa.gov/neo/rest/v1/feed/today?api_key=DEMO_KEY', parameters, 'element_count')
    if player:
        try:
            player.write_log(f"JARVIS: {result[:200]}")
        except Exception:
            pass
    return result
