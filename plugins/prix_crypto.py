"""Ported from Jarvis-Android: plugins/prix_crypto.json (http)."""
from plugins._android_runtime import run_http

PLUGIN = {
    "name": "prix_crypto",
    "description": "Donne le prix actuel d'une cryptomonnaie (bitcoin, ethereum, solana…) dans une devise. À utiliser pour « combien vaut le bitcoin ».",
    "parameters": {
        "type": "OBJECT",
        "properties": {
            "crypto": {
                "type": "STRING",
                "description": "Identifiant en minuscules : bitcoin, ethereum, solana, dogecoin…"
            },
            "devise": {
                "type": "STRING",
                "description": "Code de devise en minuscules : eur, usd, gbp… (eur par défaut)"
            }
        },
        "required": [
            "crypto"
        ]
    }
}


def run(parameters: dict, player=None, session_memory=None) -> str:
    result = run_http(PLUGIN, 'https://api.coingecko.com/api/v3/simple/price?ids={crypto}&vs_currencies={devise}', parameters)
    if player:
        try:
            player.write_log(f"JARVIS: {result[:200]}")
        except Exception:
            pass
    return result
