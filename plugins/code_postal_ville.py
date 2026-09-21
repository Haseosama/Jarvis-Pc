"""Ported from Jarvis-Android: plugins/code_postal_ville.json (http)."""
from plugins._android_runtime import run_http

PLUGIN = {
    "name": "code_postal_ville",
    "description": "Donne le code postal d'une commune française (source : adresse.data.gouv.fr). Les grandes villes ont plusieurs codes : donne alors le principal. Pour « quel est le code postal de… ».",
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
    result = run_http(PLUGIN, 'https://api-adresse.data.gouv.fr/search/?q={ville}&type=municipality&limit=1', parameters, 'features.0.properties.postcode')
    if player:
        try:
            player.write_log(f"JARVIS: {result[:200]}")
        except Exception:
            pass
    return result
