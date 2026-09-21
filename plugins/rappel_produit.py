"""Ported from Jarvis-Android: plugins/rappel_produit.json (http)."""
from plugins._android_runtime import run_http

PLUGIN = {
    "name": "rappel_produit",
    "description": "Cherche si un produit ou une marque a fait l'objet d'un rappel en France (source : RappelConso) : marque, motif, date. Pour « est-ce que le fromage X est rappelé ».",
    "parameters": {
        "type": "OBJECT",
        "properties": {
            "terme": {
                "type": "STRING",
                "description": "Nom du produit ou de la marque"
            }
        },
        "required": [
            "terme"
        ]
    }
}


def run(parameters: dict, player=None, session_memory=None) -> str:
    result = run_http(PLUGIN, 'https://data.economie.gouv.fr/api/explore/v2.1/catalog/datasets/rappelconso-v2-gtin-espaces/records?where=%22{terme}%22&limit=3&order_by=date_publication%20desc&select=marque_produit,motif_rappel,date_publication', parameters)
    if player:
        try:
            player.write_log(f"JARVIS: {result[:200]}")
        except Exception:
            pass
    return result
