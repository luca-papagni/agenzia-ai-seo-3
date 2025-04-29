import json

def load_sites():
    try:
        with open("client_sites.json", "r") as f:
            sites = json.load(f)
        return sites
    except Exception as e:
        print("❌ Errore nel caricamento siti:", e)
        return []
