"""Ported from Jarvis-Android: plugins/images_recherche.json (open)."""
from plugins._android_runtime import run_open

PLUGIN = {
    "name": "images_recherche",
    "description": "Ouvre Google Images sur une recherche. Pour « montre-moi des photos de… », « à quoi ressemble… ».",
    "parameters": {
        "type": "OBJECT",
        "properties": {
            "recherche": {
                "type": "STRING",
                "description": "Ce qu'il faut chercher en images"
            }
        },
        "required": [
            "recherche"
        ]
    }
}


def run(parameters: dict, player=None, session_memory=None) -> str:
    result = run_open(PLUGIN, 'https://www.google.com/search?tbm=isch&q={recherche}', parameters)
    if player:
        try:
            player.write_log(f"JARVIS: {result[:200]}")
        except Exception:
            pass
    return result
