import requests
import json
from datetime import date
import logging
from pathlib import Path

# Setup logging
log_dir = Path("logs")
log_dir.mkdir(exist_ok=True)
log_file = log_dir / "exchange_rate.log"

logging.basicConfig(
    filename=log_file,
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

FRANKFURTER_URL = "https://api.frankfurter.app"

def fetch_rate_for_date(target_date: date):
    response = requests.get(f"{FRANKFURTER_URL}/{target_date}")
    response.raise_for_status()
    data = response.json()

    # Log the API response
    log_data = {
        "date": target_date.isoformat(),
        "rates": data
    }
    with open(log_dir / f"{target_date}.json", "w") as f:
        json.dump(log_data, f, indent=4)
    
    logging.info(f"Fetched rate for {target_date}: {data['rates']['USD']} USD")

    return data['rates']['USD']
