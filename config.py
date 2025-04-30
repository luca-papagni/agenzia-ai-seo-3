import os
from dotenv import load_dotenv

load_dotenv()  # utile in locale, su Render non fa danni

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

# mapping  “alias_sito”  ->  { user, password }
# le credenziali arrivano da variabili d’ambiente prefissate
def wp_credentials(site_alias: str) -> dict:
    return {
        "user":     os.getenv(f"WP_{site_alias.upper()}_USER"),
        "password": os.getenv(f"WP_{site_alias.upper()}_PWD")
    }
