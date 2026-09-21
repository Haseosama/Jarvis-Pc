"""Ported from Jarvis-Android: plugins/commune_france.json (http)."""
from plugins._android_runtime import run_http

PLUGIN = {
    "name": "commune_france",
    "description": "Donne les informations d'une commune française : code INSEE, codes postaux, population et département (source : geo.api.gouv.fr). Pour « combien d'habitants à… », « dans quel département est… ».",
    "parameters": {
        "type": "OBJECT",
        "properties": {
            "ville": {
                "type": "STRING",
                "description": "Nom de la commune"
            }
        },
        "required": [
            "ville"
        ]
    }
}


def run(parameters: dict, player=None, session_memory=None) -> str:
    result = run_http(PLUGIN, 'https://geo.api.gouv.fr/communes?nom={ville}&fields=nom,code,codesPostaux,population,departement&limit=1', parameters)
    if player:
        try:
            player.write_log(f"JARVIS: {result[:200]}")
        except Exception:
            pass
    return result
