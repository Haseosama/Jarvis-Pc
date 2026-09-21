"""Ported from Jarvis-Android: plugins/phase_lune.json (http)."""
from plugins._android_runtime import run_http

PLUGIN = {
    "name": "phase_lune",
    "description": "Donne la phase de la lune aujourd'hui (un emoji) et le jour du cycle lunaire, de 0 à 29 (source : wttr.in). Pour « quelle est la phase de la lune ».",
    "parameters": {
        "type": "OBJECT",
        "properties": {
            "ville": {
                "type": "STRING",
                "description": "Nom de la ville (facultatif, la phase est la même partout)"
            }
        },
        "required": []
    }
}


def run(parameters: dict, player=None, session_memory=None) -> str:
    result = run_http(PLUGIN, 'https://wttr.in/{ville}?format=%25m+jour+%25M+du+cycle', parameters)
    if player:
        try:
            player.write_log(f"JARVIS: {result[:200]}")
        except Exception:
            pass
    return result
