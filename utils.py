import requests # type: ignore
from datetime import date

FRANKFURTER_URL = "https://api.frankfurter.app"

def fetch_rate_for_date(target_date: date):
    response = requests.get(f"{FRANKFURTER_URL}/{target_date}")
    response.raise_for_status()
    data = response.json()
    return data['rates']['USD']
