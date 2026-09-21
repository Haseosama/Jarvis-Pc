"""Ported from Jarvis-Android: plugins/definition_mot.json (open)."""
from plugins._android_runtime import run_open

PLUGIN = {
    "name": "definition_mot",
    "description": "Ouvre la définition d'un mot dans Google. Pour « que veut dire… », « la définition de… ».",
    "parameters": {
        "type": "OBJECT",
        "properties": {
            "mot": {
                "type": "STRING",
                "description": "Le mot"
            }
        },
        "required": [
            "mot"
        ]
    }
}


def run(parameters: dict, player=None, session_memory=None) -> str:
    result = run_open(PLUGIN, 'https://www.google.com/search?q=définition+{mot}', parameters)
    if player:
        try:
            player.write_log(f"JARVIS: {result[:200]}")
        except Exception:
            pass
    return result
