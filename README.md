# Knicks / Brunson Shot Profile

Data analytics + ComfyUI visual project focused on Jalen Brunson and the New York Knicks shot patterns.

## Goal
Analyze Brunson’s (and Knicks) shot profile using public NBA data, extract clear insights, and generate supporting visuals with ComfyUI for a LinkedIn-ready portfolio piece.

## Project Structure
```
knicks-brunson-shot-profile/
├── data/                  # Raw and processed CSVs
├── notebooks/             # Jupyter notebooks for exploration
├── src/                   # Python modules / scripts
├── outputs/               # Charts, reports, final images
├── comfyui/               # Prompts, workflows, reference images
├── requirements.txt
└── README.md
```

## Quick Start

1. Clone and set up:
   ```bash
   git clone <your-repo-url>
   cd knicks-brunson-shot-profile
   python -m venv venv
   source venv/bin/activate  # or venv\Scripts\activate on Windows
   pip install -r requirements.txt
   ```

2. Pull shot data:
   ```bash
   python src/pull_shot_data.py
   ```

3. Open the notebook in `notebooks/` to explore and generate charts.

## Data Sources
- `nba_api` (ShotChartDetail and related endpoints)
- Basketball-Reference for validation

## ComfyUI
Place reference poses, prompts, and exported workflows in the `comfyui/` folder.

## License
MIT
