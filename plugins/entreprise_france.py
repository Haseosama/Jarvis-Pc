"""Ported from Jarvis-Android: plugins/entreprise_france.json (http)."""
from plugins._android_runtime import run_http

PLUGIN = {
    "name": "entreprise_france",
    "description": "Retrouve une entreprise française par son nom : raison sociale, numéro SIREN, adresse du siège, activité (source : recherche-entreprises.api.gouv.fr). Donne la meilleure correspondance du nom : mieux vaut le nom complet. Pour « c'est quoi cette société », « le SIREN de… ».",
    "parameters": {
        "type": "OBJECT",
        "properties": {
            "nom": {
                "type": "STRING",
                "description": "Nom complet de l'entreprise"
            }
        },
        "required": [
            "nom"
        ]
    }
}


def run(parameters: dict, player=None, session_memory=None) -> str:
    result = run_http(PLUGIN, 'https://recherche-entreprises.api.gouv.fr/search?q={nom}&per_page=1', parameters)
    if player:
        try:
            player.write_log(f"JARVIS: {result[:200]}")
        except Exception:
            pass
    return result
