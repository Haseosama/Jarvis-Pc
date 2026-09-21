"""Ported from Jarvis-Android: plugins/lever_coucher_soleil.json (http)."""
from plugins._android_runtime import run_http

PLUGIN = {
    "name": "lever_coucher_soleil",
    "description": "Donne l'heure de lever et de coucher du soleil aujourd'hui, heure locale de la ville (source : wttr.in). Sans ville, le service se base sur l'adresse réseau du téléphone. Pour « à quelle heure se couche le soleil ».",
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
    result = run_http(PLUGIN, 'https://wttr.in/{ville}?format=Lever+%25S,+coucher+%25s', parameters)
    if player:
        try:
            player.write_log(f"JARVIS: {result[:200]}")
        except Exception:
            pass
    return result
