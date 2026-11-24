import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.patches import Circle, Rectangle, Arc, Polygon
import numpy as np

def draw_court(ax=None, color='black', lw=1):
    if ax is None:
        ax = plt.gca()
    hoop = Circle((0, 0), radius=7.5, linewidth=lw, color=color, fill=False)
    backboard = Rectangle((-30, -7.5), 60, -1, linewidth=lw, color=color)
    paint = Rectangle((-80, -47.5), 160, 190, linewidth=lw, color=color, fill=False)
    free_throw = Circle((0, 142.5), radius=60, linewidth=lw, color=color, fill=False)
    three_arc = Arc((0, 0), 475, 475, theta1=22, theta2=158, linewidth=lw, color=color)
    ax.add_patch(hoop)
    ax.add_patch(backboard)
    ax.add_patch(paint)
    ax.add_patch(free_throw)
    ax.add_patch(three_arc)
    ax.set_xlim(-250, 250)
    ax.set_ylim(-47.5, 422.5)
    ax.set_aspect('equal')

# Load data
reg = pd.read_csv("data/brunson_shots_2025_26_regular_season.csv")
play = pd.read_csv("data/brunson_shots_2025_26_playoffs.csv")

# Calculate share change by zone
def zone_share(df):
    return df.groupby("SHOT_ZONE_BASIC").size() / len(df)

reg_share = zone_share(reg)
play_share = zone_share(play)
change = (play_share - reg_share).fillna(0) * 100  # percentage point change

print("Shot share change (playoffs - regular season):")
print(change.round(1))

# Simple zone coloring on court
fig, ax = plt.subplots(figsize=(10, 9))
draw_court(ax)

# Restricted Area (biggest increase)
ra = Circle((0, 0), radius=40, color='#2ca02c', alpha=0.35, label='Restricted Area +11 pts')
ax.add_patch(ra)

# Mid-range drop (approximate area)
mid = Rectangle((-100, 50), 200, 120, color='#d62728', alpha=0.25, label='Mid-Range efficiency drop')
ax.add_patch(mid)

ax.set_title("Brunson Shot Diet Shift: Playoffs vs Regular Season\nGreen = more volume, Red = efficiency drop", fontsize=12)
ax.legend(loc='upper right')
plt.savefig("outputs/zone_shift_court.png", dpi=150, bbox_inches="tight")
print("\nSaved outputs/zone_shift_court.png")