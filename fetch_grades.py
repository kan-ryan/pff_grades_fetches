import requests
from config import SUMMARY_URL, COOKIES
from export_utils import export_to_csv

def fetch_summary_grades(game_id):
    params = {"game_id": game_id}
    response = requests.get(SUMMARY_URL, params=params, cookies=COOKIES)
    response.raise_for_status()
    return response.json()["offense_summary"]

def main():
    game_id = input("Enter Game ID: ")
    grades = fetch_summary_grades(game_id)
    export_to_csv(grades, f"grades_{game_id}.csv")
    print(f"Exported {len(grades)} player grade rows to grades_{game_id}.csv")

if __name__ == "__main__":
    main()
