import requests
from pathlib import Path
import json
from datetime import datetime

OUT = Path("data_raw/public")
OUT.mkdir(parents=True, exist_ok=True)

url = "https://people.sc.fsu.edu/~jburkardt/data/csv/airtravel.csv"

response = requests.get(url, timeout=20)
response.raise_for_status()

(OUT / "airtravel.csv").write_bytes(response.content)

metadata = {
    "source": url,
    "downloaded_at": datetime.utcnow().isoformat() + "Z",
    "description": "Flight stats dataset"
}
(OUT / "metadata.json").write_text(json.dumps(metadata, indent=2))
