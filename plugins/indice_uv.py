"""Ported from Jarvis-Android: plugins/indice_uv.json (http)."""
from plugins._android_runtime import run_http

PLUGIN = {
    "name": "indice_uv",
    "description": "Donne l'indice UV actuel d'une ville (source : wttr.in). 0 à 2 faible, 3 à 5 modéré, 6 à 7 fort, 8 et plus très fort. Sans ville, d'après l'adresse réseau du téléphone. Pour « faut-il mettre de la crème solaire ».",
    "parameters": {
        "type": "OBJECT",
        "properties": {
            "ville": {
                "type": "STRING",
                "description": "Nom de la ville (facultatif)"
            }
        },
        "required": []
    }
}


def run(parameters: dict, player=None, session_memory=None) -> str:
    result = run_http(PLUGIN, 'https://wttr.in/{ville}?format=UV+%25u', parameters)
    if player:
        try:
            player.write_log(f"JARVIS: {result[:200]}")
        except Exception:
            pass
    return result
