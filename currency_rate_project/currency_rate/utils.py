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
    try:
        response = requests.get(f"{FRANKFURTER_URL}/{target_date}?from=USD&to=EUR")
        response.raise_for_status()
        data = response.json()

        # Log the API response
        log_data = {
            "date": target_date.isoformat(),
            "rates": data
        }
        with open(log_dir / f"{target_date}.json", "w") as f:
            json.dump(log_data, f, indent=4)
        
        logging.info(f"Fetched rate for {target_date}: {data['rates']['EUR']} EUR")

        return data['rates']['EUR']
    except requests.RequestException as e:
        logging.error(f"Error fetching rate for {target_date}: {e}")
        raise e
