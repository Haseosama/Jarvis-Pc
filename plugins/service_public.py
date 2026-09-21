"""Ported from Jarvis-Android: plugins/service_public.json (open)."""
from plugins._android_runtime import run_open

PLUGIN = {
    "name": "service_public",
    "description": "Ouvre la recherche de service-public.fr sur une démarche ou un droit (carte d'identité, permis, carte grise, allocations…). Pour « comment faire ma carte d'identité ».",
    "parameters": {
        "type": "OBJECT",
        "properties": {
            "sujet": {
                "type": "STRING",
                "description": "La démarche ou le sujet"
            }
        },
        "required": [
            "sujet"
        ]
    }
}


def run(parameters: dict, player=None, session_memory=None) -> str:
    result = run_open(PLUGIN, 'https://www.service-public.fr/particuliers/recherche?keyword={sujet}', parameters)
    if player:
        try:
            player.write_log(f"JARVIS: {result[:200]}")
        except Exception:
            pass
    return result
