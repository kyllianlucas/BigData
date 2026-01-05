import requests
import csv
import os

URL = "https://tabular-api.data.gouv.fr/api/resources/1c5075ec-7ce1-49cb-ab89-94f507812daf/data/"

def fetch_and_save():
    base_dir = os.path.dirname(os.path.abspath(__file__))
    data_dir = os.path.join(base_dir, "data")
    os.makedirs(data_dir, exist_ok=True)

    rows = []
    next_url = URL

    while next_url and len(rows) < 100:
        resp = requests.get(next_url, timeout=10)
        resp.raise_for_status()

        data = resp.json()
        rows.extend(data["data"])
        next_url = data["links"].get("next")

    rows = rows[:100]

    output_file = os.path.join(data_dir, "data_raw_100.csv")

    with open(output_file, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=rows[0].keys())
        writer.writeheader()
        writer.writerows(rows)

    print(f"Fichier créé : {output_file}")