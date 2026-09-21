"""Ported from Jarvis-Android: plugins/classement_f1.json (http)."""
from plugins._android_runtime import run_http

PLUGIN = {
    "name": "classement_f1",
    "description": "Donne le classement actuel du championnat de Formule 1 des pilotes : les 3 premiers avec points et victoires (source : Jolpica, successeur d'Ergast). Pour « qui mène en F1 ».",
    "parameters": {
        "type": "OBJECT",
        "properties": {},
        "required": []
    }
}


def run(parameters: dict, player=None, session_memory=None) -> str:
    result = run_http(PLUGIN, 'https://api.jolpi.ca/ergast/f1/current/driverStandings.json?limit=3', parameters)
    if player:
        try:
            player.write_log(f"JARVIS: {result[:200]}")
        except Exception:
            pass
    return result
