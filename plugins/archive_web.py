"""Ported from Jarvis-Android: plugins/archive_web.json (http)."""
from plugins._android_runtime import run_http

PLUGIN = {
    "name": "archive_web",
    "description": "Donne le lien vers la copie la plus proche d'un site dans la Wayback Machine d'Internet Archive. Pour « à quoi ressemblait ce site avant », « ce site a disparu ».",
    "parameters": {
        "type": "OBJECT",
        "properties": {
            "adresse": {
                "type": "STRING",
                "description": "Adresse du site, par exemple example.com"
            }
        },
        "required": [
            "adresse"
        ]
    }
}


def run(parameters: dict, player=None, session_memory=None) -> str:
    result = run_http(PLUGIN, 'https://archive.org/wayback/available?url={adresse}', parameters, 'archived_snapshots.closest.url')
    if player:
        try:
            player.write_log(f"JARVIS: {result[:200]}")
        except Exception:
            pass
    return result
