"""Ported from Jarvis-Android: plugins/synonymes.json (open)."""
from plugins._android_runtime import run_open

PLUGIN = {
    "name": "synonymes",
    "description": "Ouvre les synonymes d'un mot (CNRTL). Pour « un synonyme de… », « comment dire autrement… ».",
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
    result = run_open(PLUGIN, 'https://www.cnrtl.fr/synonymie/{mot}', parameters)
    if player:
        try:
            player.write_log(f"JARVIS: {result[:200]}")
        except Exception:
            pass
    return result
