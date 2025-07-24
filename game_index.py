import requests
from config import COOKIES


def get_game_ids(franchise_id, season, weeks=None):
    if weeks is None:
        weeks = ",".join(str(w) for w in range(0, 17))  # Weeks 0–16

    url = "https://premium.pff.com/api/v1/teams/summary"
    params = {
        "league": "ncaa",
        "season": season,
        "franchise_id": franchise_id,
        "week": weeks
    }

    res = requests.get(url, params=params, cookies=COOKIES)
    res.raise_for_status()
    data = res.json()

    # The correct key from your screenshot is 'team_summary'
    game_ids = []
    for game in data.get("team_summary", []):
        game_id = game.get("game_id")
        if game_id and game_id not in game_ids:
            game_ids.append(game_id)

    return game_ids


if __name__ == "__main__":
    franchise_id = 103  
    season = 2022

    game_ids = get_game_ids(franchise_id, season)
    print(f"Found {len(game_ids)} game IDs:", game_ids)
