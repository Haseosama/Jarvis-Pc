"""Ported from Jarvis-Android: plugins/rappels_recents.json (http)."""
from plugins._android_runtime import run_http

PLUGIN = {
    "name": "rappels_recents",
    "description": "Donne les 4 derniers rappels de produits de consommation en France : catégorie, marque, motif et date (source : RappelConso, data.economie.gouv.fr). Pour « y a-t-il des rappels de produits », « un produit dangereux ».",
    "parameters": {
        "type": "OBJECT",
        "properties": {},
        "required": []
    }
}


def run(parameters: dict, player=None, session_memory=None) -> str:
    result = run_http(PLUGIN, 'https://data.economie.gouv.fr/api/explore/v2.1/catalog/datasets/rappelconso-v2-gtin-espaces/records?limit=4&order_by=date_publication%20desc&select=categorie_produit,marque_produit,motif_rappel,date_publication', parameters)
    if player:
        try:
            player.write_log(f"JARVIS: {result[:200]}")
        except Exception:
            pass
    return result
