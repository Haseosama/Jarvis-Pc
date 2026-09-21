"""Ported from Jarvis-Android: plugins/vacances_scolaires.json (http)."""
from plugins._android_runtime import run_http

PLUGIN = {
    "name": "vacances_scolaires",
    "description": "Donne les 2 prochaines périodes de vacances scolaires d'une zone (A, B ou C), avec dates de début et de fin en UTC : en France, ajouter 1 h (hiver) ou 2 h (été) donne minuit local (source : data.education.gouv.fr). Pour « quand sont les prochaines vacances ».",
    "parameters": {
        "type": "OBJECT",
        "properties": {
            "zone": {
                "type": "STRING",
                "description": "Zone A, Zone B ou Zone C (écrire exactement ainsi)"
            }
        },
        "required": [
            "zone"
        ]
    }
}


def run(parameters: dict, player=None, session_memory=None) -> str:
    result = run_http(PLUGIN, 'https://data.education.gouv.fr/api/explore/v2.1/catalog/datasets/fr-en-calendrier-scolaire/records?where=zones%3D%22{zone}%22%20AND%20end_date%3E%3Dnow()&order_by=start_date&limit=2&select=description,start_date,end_date', parameters)
    if player:
        try:
            player.write_log(f"JARVIS: {result[:200]}")
        except Exception:
            pass
    return result
