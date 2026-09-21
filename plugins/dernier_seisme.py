"""Ported from Jarvis-Android: plugins/dernier_seisme.json (http)."""
from plugins._android_runtime import run_http

PLUGIN = {
    "name": "dernier_seisme",
    "description": "Donne le dernier séisme de magnitude 4,5 ou plus des dernières 24 heures dans le monde (source : USGS) : magnitude et lieu, en anglais. Pour « y a-t-il eu un tremblement de terre ? ».",
    "parameters": {
        "type": "OBJECT",
        "properties": {},
        "required": []
    }
}


def run(parameters: dict, player=None, session_memory=None) -> str:
    result = run_http(PLUGIN, 'https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/4.5_day.geojson', parameters, 'features.0.properties.title')
    if player:
        try:
            player.write_log(f"JARVIS: {result[:200]}")
        except Exception:
            pass
    return result
