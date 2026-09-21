"""Ported from Jarvis-Android: plugins/adresse_france.json (http)."""
from plugins._android_runtime import run_http

PLUGIN = {
    "name": "adresse_france",
    "description": "Retrouve une adresse postale en France avec son code postal et sa ville (source : Base Adresse Nationale, adresse.data.gouv.fr). Base d'adresses : les monuments et les commerces ne sont pas toujours reconnus, donner un numéro et une rue. Pour « c'est quel code postal au 10 rue de… ».",
    "parameters": {
        "type": "OBJECT",
        "properties": {
            "recherche": {
                "type": "STRING",
                "description": "Adresse, par exemple 10 rue de la paix Paris"
            }
        },
        "required": [
            "recherche"
        ]
    }
}


def run(parameters: dict, player=None, session_memory=None) -> str:
    result = run_http(PLUGIN, 'https://api-adresse.data.gouv.fr/search/?q={recherche}&limit=1', parameters, 'features.0.properties.label')
    if player:
        try:
            player.write_log(f"JARVIS: {result[:200]}")
        except Exception:
            pass
    return result
