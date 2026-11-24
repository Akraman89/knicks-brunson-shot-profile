import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.patches import Circle, Rectangle, Arc

st.set_page_config(page_title="Brunson Shot Profile", layout="wide")
st.title("Jalen Brunson Shot Profile: Regular Season vs Playoffs")

reg = pd.read_csv("data/brunson_shots_2025_26_regular_season.csv")
play = pd.read_csv("data/brunson_shots_2025_26_playoffs.csv")

col1, col2, col3 = st.columns(3)
col1.metric("Reg Season FG%", f"{reg['SHOT_MADE_FLAG'].mean()*100:.1f}%")
col2.metric("Playoff FG%", f"{play['SHOT_MADE_FLAG'].mean()*100:.1f}%")
col3.metric("Distance Change", f"{play['SHOT_DISTANCE'].mean() - reg['SHOT_DISTANCE'].mean():.1f} ft")

st.subheader("Zone Share Change (Playoffs - Regular Season)")
def zone_share(df):
    return df.groupby("SHOT_ZONE_BASIC").size() / len(df) * 100

change = (zone_share(play) - zone_share(reg)).round(1).sort_values(ascending=False)
st.bar_chart(change)

st.subheader("Shot Charts")
col_a, col_b = st.columns(2)
col_a.image("outputs/brunson_reg_season.png", caption="Regular Season")
col_b.image("outputs/brunson_playoffs.png", caption="Playoffs")