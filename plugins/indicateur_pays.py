"""Ported from Jarvis-Android: plugins/indicateur_pays.json (http)."""
from plugins._android_runtime import run_http

PLUGIN = {
    "name": "indicateur_pays",
    "description": "Donne un indicateur statistique d'un pays, avec l'année de la donnée (source : Banque mondiale). Pour « combien d'habitants en… », « le PIB de… », « l'espérance de vie au… ».",
    "parameters": {
        "type": "OBJECT",
        "properties": {
            "pays": {
                "type": "STRING",
                "description": "Code pays à 2 lettres en minuscules : fr, de, us, jp, br, in, ma, sn…"
            },
            "indicateur": {
                "type": "STRING",
                "description": "SP.POP.TOTL population, NY.GDP.MKTP.CD PIB en dollars, SP.DYN.LE00.IN espérance de vie, SL.UEM.TOTL.ZS chômage en %, EN.ATM.CO2E.PC CO2 par habitant"
            }
        },
        "required": [
            "pays",
            "indicateur"
        ]
    }
}


def run(parameters: dict, player=None, session_memory=None) -> str:
    result = run_http(PLUGIN, 'https://api.worldbank.org/v2/country/{pays}/indicator/{indicateur}?format=json&per_page=1&mrnev=1', parameters)
    if player:
        try:
            player.write_log(f"JARVIS: {result[:200]}")
        except Exception:
            pass
    return result
