"""Ported from Jarvis-Android: plugins/meteo_aeroport.json (http)."""
from plugins._android_runtime import run_http

PLUGIN = {
    "name": "meteo_aeroport",
    "description": "Donne le dernier bulletin météo d'un aéroport au format METAR (source : aviationweather.gov) : à décoder et à expliquer (vent, visibilité, température, pression). Pour « le temps à l'aéroport de… », « la météo de Roissy ».",
    "parameters": {
        "type": "OBJECT",
        "properties": {
            "icao": {
                "type": "STRING",
                "description": "Code OACI de l'aéroport à 4 lettres : LFPG Paris-CDG, LFPO Orly, LFML Marseille, LFLL Lyon, LFBO Toulouse, LFMN Nice, EGLL Londres, KJFK New York"
            }
        },
        "required": [
            "icao"
        ]
    }
}


def run(parameters: dict, player=None, session_memory=None) -> str:
    result = run_http(PLUGIN, 'https://aviationweather.gov/api/data/metar?ids={icao}&format=raw', parameters)
    if player:
        try:
            player.write_log(f"JARVIS: {result[:200]}")
        except Exception:
            pass
    return result
