# CAISO Interconnection Queue Intelligence

Interconnection queues have become a major bottleneck in California’s clean energy transition. Every year, hundreds of proposed generation and storage projects enter CAISO’s interconnection queue, yet most never reach completion. Although CAISO publishes public data on these projects, the information is released as fragmented, static Excel files that are difficult to analyze over time or across locations. This project grew out of a desire to use data analytics to better understand a real, high-impact energy systems problem. Interconnection queues stood out because they quietly shape which clean energy projects move forward and which stall, while still offering publicly available data to work with. Using only CAISO’s public disclosures, this repository organizes, cleans, and analyzes interconnection queue data to explore a few big-picture questions: which projects tend to survive, when withdrawals usually happen, what kinds of technologies are entering the queue today, and where interconnection demand is most concentrated across California. The goal is not to make predictions, but to make an opaque and important system easier to understand through clear, transparent analysis.

## Scope & Design 

This project is intentionally retrospective and descriptive rather than predictive. The goal is to understand how California’s interconnection queue has behaved using only what can be clearly observed in public CAISO data, without trying to forecast outcomes or fill in missing information with assumptions. Throughout the project, I prioritized careful, defensible analysis over broader claims that the data cannot reliably support.

Within these boundaries, the analysis looks at queue outcomes, survivability and timing patterns, cohort behavior in Cluster 15, and intake composition across Cluster 14 and Cluster 15, using megawatt-weighted metrics and basic spatial analysis to highlight patterns by technology, scale, and location. The project intentionally leaves out project-level tracking across years, cost or study-stage analysis, developer behavior, prediction, and any non-public data, keeping the focus on transparency and what the public data can credibly show.

Here is the 6-Page Report that pairs with this Github Repo

https://docs.google.com/document/d/19qYg5qzphvVOD21XKS8pSuLvm1Si27LU-fXW6xHcSv4/edit?usp=sharing

## Data Sources

The analysis uses only public CAISO files:

1. **Public Queue Report (`public_queue_report.xlsx`)**  
   A system-wide snapshot of active, withdrawn, and completed interconnection requests across all cohorts.

2. **Cluster 15 Interconnection Requests (`cluster15_interconnection_requests.xlsx`)**  
   A single, internally consistent intake cohort with richer project attributes, enabling clean survivability analysis.

3. **Preliminary Cluster 14 Project List (`preliminary_cluster14_project_list.xlsx`)**  
   A historical intake snapshot used to evaluate **how queue composition has changed over time**.


## Repository Structure

```
├─ README.md
├─ requirements.txt
├─ data/
│ ├─ raw/                     
│ ├─ processed/               
│ └─ gis/
├─ notebooks/
│ ├─ 01_data_management.ipynb
│ ├─ 02_clean_public_queue.ipynb
│ ├─ 03_clean_cluster15.ipynb
│ ├─ 04_clean_cluster14.ipynb
│ ├─ 05_survivability_analysis.ipynb
│ └─ 06_spatial_analysis.ipynb
├─ outputs/
│ ├─ survivability/
│ └─ spatial/
```
## Notebooks

These notebooks are meant to be run in order. Together, they form a transparent pipeline: start by inspecting the raw CAISO files, then clean them into consistent, analysis-ready tables, and finally produce the survivability and spatial results. The notebooks focus on what public CAISO data can clearly support (outcomes, timing, technology mix, MW-weighted patterns, and geography), and they do not attempt project-level tracking across years, study-stage analysis, cost estimates, or prediction.

### 01_data_management.ipynb
Inventories the raw files, documents what fields exist (and what is missing), and sets up the project’s folder paths and outputs. This notebook is about establishing boundaries and structure, not producing final findings.

### 02_clean_public_queue.ipynb
Cleans and standardizes the system-wide Public Queue Report into a consistent processed dataset. This enables aggregate outcome and timing analysis, but it does not create longitudinal project histories across reporting years.

### 03_clean_cluster15.ipynb
Cleans and canonicalizes Cluster 15 intake data into a cohort dataset with consistent technology and capacity fields. This is the main cohort used for survivability-style comparisons within a shared intake framework.

### 04_clean_cluster14.ipynb
Cleans the Cluster 14 intake snapshot (with more limited public fields) to support intake composition and basic geographic comparisons. It is not used for deeper survivability timing because the public detail is thinner.

### 05_survivability_analysis.ipynb
Uses the processed public queue and Cluster 15 data to summarize outcomes, withdrawal timing patterns, and MW-weighted survivability differences by technology and size. It is descriptive only and avoids prediction or causal claims.

### 06_spatial_analysis.ipynb
Uses processed datasets plus the county GeoJSON to map and summarize county-level and POI-level concentration patterns. The maps show where queue pressure clusters, but they do not explain why a specific site succeeds or fails.

## Key Findings (High-Level)

Across the analyses:
* Withdrawal is the dominant outcome in the CAISO interconnection process
* Attrition is front-loaded, with many projects withdrawing relatively early after queue entry
* Project scale matters: large projects dominate proposed MW and show meaningfully lower withdrawal rates
* Technology differences are closely tied to scale, rather than acting as standalone drivers of survivability
* Recent intake composition differs from historical completions, suggesting a mismatch between what enters the queue and what has historically finished
* Spatial patterns show regional clustering of both proposed capacity and attrition, though precision is limited by public data granularity

Taken together, the results suggest survivability is shaped most by feasibility, scale, and economic robustness, not any single attribute.

## Reproducibility
All results can be reproduced by creating a virtual environment, installing dependencies, and running the notebooks in order:

```
python -m venv .venv
source .venv/bin/activate   # or .venv\Scripts\activate on Windows
pip install -r requirements.txt
jupyter lab
```
