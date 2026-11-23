"""
Pull Jalen Brunson shot chart data using nba_api.
Saves raw CSVs to the data/ folder.
"""

import os
from nba_api.stats.endpoints import shotchartdetail
from nba_api.stats.static import players
import pandas as pd

# Find Brunson's player ID
player_dict = players.get_players()
brunson = [p for p in player_dict if p["full_name"] == "Jalen Brunson"][0]
PLAYER_ID = brunson["id"]
print(f"Brunson player ID: {PLAYER_ID}")

# Seasons to pull (championship year + prior)
SEASONS = ["2024-25", "2025-26"]
SEASON_TYPES = ["Regular Season", "Playoffs"]

os.makedirs("../data", exist_ok=True)

for season in SEASONS:
    for season_type in SEASON_TYPES:
        print(f"Pulling {season} {season_type}...")
        try:
            shot_data = shotchartdetail.ShotChartDetail(
                team_id=0,
                player_id=PLAYER_ID,
                season_nullable=season,
                season_type_all_star=season_type,
                context_measure_simple="FGA"
            )
            df = shot_data.shot_chart_detail.get_data_frame()
            filename = f"../data/brunson_shots_{season.replace('-', '_')}_{season_type.replace(' ', '_').lower()}.csv"
            df.to_csv(filename, index=False)
            print(f"  Saved {len(df)} shots → {filename}")
        except Exception as e:
            print(f"  Failed for {season} {season_type}: {e}")

print("Done.")
