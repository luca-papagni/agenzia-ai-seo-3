import json, pathlib

SITE_FILE = pathlib.Path("sites.json")

def all_sites() -> list[dict]:
    with SITE_FILE.open() as f:
        raw = json.load(f)
    return raw             # [{alias, url, topic}]
