"""Ported from Jarvis-Android: plugins/prix_carburant.json (http)."""
from plugins._android_runtime import run_http

PLUGIN = {
    "name": "prix_carburant",
    "description": "Donne les 3 stations les moins chères d'une ville en France pour un carburant, avec leur adresse et leur prix au litre en euros (source : data.economie.gouv.fr). Pour « où est l'essence la moins chère à Lyon ».",
    "parameters": {
        "type": "OBJECT",
        "properties": {
            "ville": {
                "type": "STRING",
                "description": "Nom de la ville (la recherche couvre aussi les communes de même nom)"
            },
            "carburant": {
                "type": "STRING",
                "description": "Un de : gazole_prix, e10_prix, sp95_prix, sp98_prix, e85_prix, gplc_prix"
            }
        },
        "required": [
            "ville",
            "carburant"
        ]
    }
}


def run(parameters: dict, player=None, session_memory=None) -> str:
    result = run_http(PLUGIN, 'https://data.economie.gouv.fr/api/explore/v2.1/catalog/datasets/prix-des-carburants-en-france-flux-instantane-v2/records?where=search(ville%2C%22{ville}%22)&order_by={carburant}&limit=3&select=adresse,ville,{carburant}', parameters)
    if player:
        try:
            player.write_log(f"JARVIS: {result[:200]}")
        except Exception:
            pass
    return result
