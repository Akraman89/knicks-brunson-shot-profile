import pandas as pd

reg = pd.read_csv("data/brunson_shots_2025_26_regular_season.csv")
play = pd.read_csv("data/brunson_shots_2025_26_playoffs.csv")

def zone_summary(df, label):
    summary = df.groupby("SHOT_ZONE_BASIC").agg(
        shots=("SHOT_MADE_FLAG", "count"),
        makes=("SHOT_MADE_FLAG", "sum"),
        fg_pct=("SHOT_MADE_FLAG", "mean")
    ).reset_index()
    summary["fg_pct"] = (summary["fg_pct"] * 100).round(1)
    summary["share"] = (summary["shots"] / summary["shots"].sum() * 100).round(1)
    summary["season"] = label
    return summary

reg_zones = zone_summary(reg, "Regular Season")
play_zones = zone_summary(play, "Playoffs")

combined = pd.concat([reg_zones, play_zones])
print(combined.sort_values(["SHOT_ZONE_BASIC", "season"]).to_string(index=False))

# Save for later
combined.to_csv("outputs/zone_comparison.csv", index=False)
print("\nSaved to outputs/zone_comparison.csv")