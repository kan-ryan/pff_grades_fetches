## PFF Grades Fetcher

This is a simple Python project to fetch player grades from PFF FC's API and export them to CSV.

## Setup
1. Clone or download this repo.
2. Open `config.py` and paste your session cookies from Chrome DevTools (instructions below).
3. (Optional) Create a virtualenv and install dependencies (just `requests`).

```bash
python3 -m venv venv
source venv/bin/activate
pip install requests
```

## Usage
```bash
python fetch_grades.py
```
Enter the game ID when prompted. The grades will be saved to a CSV file named like `grades_26200.csv`.

## Getting Your PFF Session Cookies
- Open [https://premium.pff.com](https://premium.pff.com) and log in
- Open **Chrome DevTools > Network tab**
- Reload a page showing player grades (like Georgia Tech offense page)
- Click on a request like `summary?game_id=...`
- Go to the **Headers** tab
- Under **Request Headers**, find the `cookie` field
- Copy values for:
  - `_premium_key`
  - `c_groot_access_token`
  - `c_groot_refresh_token`
- Paste them into `config.py` under `COOKIES`

## Important: Session Cookies Expire
These cookies usually expire within 12–24 hours. If your script stops working and you get a 401 error:
- Re-open DevTools
- Refresh a grades page
- Copy fresh cookies into `config.py`

---
Let me know if you want to:
- Scrape multiple games at once
- Filter by team/position/week
- Export JSON or load to a database
- Automate login to refresh cookies without DevTools

Happy data hunting 🏈