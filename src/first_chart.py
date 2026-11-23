import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.patches import Circle, Rectangle, Arc

def draw_court(ax=None, color='black', lw=1):
    if ax is None:
        ax = plt.gca()
    hoop = Circle((0, 0), radius=7.5, linewidth=lw, color=color, fill=False)
    backboard = Rectangle((-30, -7.5), 60, -1, linewidth=lw, color=color)
    paint = Rectangle((-80, -47.5), 160, 190, linewidth=lw, color=color, fill=False)
    free_throw = Circle((0, 142.5), radius=60, linewidth=lw, color=color, fill=False)
    three_arc = Arc((0, 0), 475, 475, theta1=22, theta2=158, linewidth=lw, color=color)
    corner_three_left = Rectangle((-250, -47.5), 0, 140, linewidth=lw, color=color)
    corner_three_right = Rectangle((250, -47.5), 0, 140, linewidth=lw, color=color)
    ax.add_patch(hoop)
    ax.add_patch(backboard)
    ax.add_patch(paint)
    ax.add_patch(free_throw)
    ax.add_patch(three_arc)
    ax.add_patch(corner_three_left)
    ax.add_patch(corner_three_right)
    ax.set_xlim(-250, 250)
    ax.set_ylim(-47.5, 422.5)
    ax.set_aspect('equal')

df = pd.read_csv("data/brunson_shots_2025_26_regular_season.csv")
fig, ax = plt.subplots(figsize=(12, 11))
draw_court(ax)
makes = df[df["SHOT_MADE_FLAG"] == 1]
misses = df[df["SHOT_MADE_FLAG"] == 0]
ax.scatter(misses["LOC_X"], misses["LOC_Y"], c="red", alpha=0.5, s=15, label="Miss")
ax.scatter(makes["LOC_X"], makes["LOC_Y"], c="green", alpha=0.6, s=15, label="Make")
ax.set_title("Jalen Brunson Shot Chart - 2025-26 Regular Season", fontsize=14)
ax.legend()
plt.savefig("outputs/brunson_shot_chart_court.png", dpi=150, bbox_inches="tight")
print("Saved outputs/brunson_shot_chart_court.png")
