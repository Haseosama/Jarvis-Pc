"""Ported from Jarvis-Android: plugins/agenda_evenement.json (open)."""
from plugins._android_runtime import run_open

PLUGIN = {
    "name": "agenda_evenement",
    "description": "Ouvre Google Agenda avec un nouvel événement prérempli (titre et lieu). L'utilisateur choisit la date et valide. Pour « ajoute un rendez-vous ».",
    "parameters": {
        "type": "OBJECT",
        "properties": {
            "titre": {
                "type": "STRING",
                "description": "Titre de l'événement"
            },
            "lieu": {
                "type": "STRING",
                "description": "Lieu (facultatif)"
            }
        },
        "required": [
            "titre"
        ]
    }
}


def run(parameters: dict, player=None, session_memory=None) -> str:
    result = run_open(PLUGIN, 'https://calendar.google.com/calendar/render?action=TEMPLATE&text={titre}&location={lieu}', parameters)
    if player:
        try:
            player.write_log(f"JARVIS: {result[:200]}")
        except Exception:
            pass
    return result
