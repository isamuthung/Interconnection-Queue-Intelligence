# CAISO Interconnection Queue Survivability & Intake Analysis

## Overview

This repository contains a **reproducible, public-data analysis of the CAISO generator interconnection queue**, focused on **project survivability, attrition, intake composition, and spatial patterns**.

Using only **publicly available CAISO disclosures**, the project examines:

- which types of projects tend to **withdraw vs persist**,
- **when** attrition occurs,
- how **intake composition has evolved across cohorts**, and
- how survivability patterns vary across **technology, scale, and geography**.

The emphasis is on **interpretability, clean data pipelines, and methodological honesty** rather than black-box prediction. The result is an analysis that is useful for understanding **structural interconnection risk** while clearly documenting the limits of what public data can support.

## Motivation

Interconnection queues are now one of the largest bottlenecks to clean energy deployment in the United States. In CAISO, hundreds of generation and storage projects enter the queue each year, yet **a majority never reach completion**.

While CAISO publishes queue data, it is:
- provided as **static snapshots**,  
- fragmented across multiple files and cohorts, and  
- not structured for direct analytics or longitudinal analysis.

This project reorganizes those disclosures into **analysis-ready datasets** and uses them to surface **systematic patterns of attrition, persistence, and mismatch** that are not obvious from raw queue reports.

## Scope & Design Philosophy

This project is **retrospective and descriptive**, not predictive.

### In scope
- Observed outcomes (active / withdrawn / completed)
- Cohort-level survivability (Cluster 15)
- Intake comparison across cohorts (Cluster 14 vs 15)
- Intake vs historical completion **distribution mismatch**
- County-level spatial patterns using public geographic boundaries

### Explicitly out of scope (by design)
- Per-project longitudinal tracking across years
- Internal CAISO study stages, restudies, or cost assignments
- Market Participant Portal or non-public data
- Machine-learning or predictive risk scoring

This design prioritizes **credible inference over over-reach**.

## Data Sources

The analysis uses **only public CAISO files**:

1. **Public Queue Report (`publicqueuereport.xlsx`)**  
   A system-wide snapshot of active, withdrawn, and completed interconnection requests across all cohorts.

2. **Cluster 15 Interconnection Requests (`cluster-15-interconnection-requests.xlsx`)**  
   A single intake cohort with consistent rules and rich project attributes, enabling clean survivability analysis.

3. **Preliminary Cluster 14 Project List (`PreliminaryCluster14ProjectListasofMay20-2021.xlsx`)**  
   A historical intake snapshot used to study **how queue composition has changed over time**.

No APIs, scraping, or restricted portals are used.

## Repository Structure

```
├─ README.md
├─ requirements.txt
├─ data/
│  ├─ raw/          # Original CAISO XLSX files (unchanged)
│  └─ processed/    # Cleaned, canonical analysis tables
├─ notebooks/
│  ├─ 01_data_inventory.ipynb
│  ├─ 02_clean_public_queue.ipynb
│  ├─ 03_clean_cluster15.ipynb
│  ├─ 04_survivability_insights.ipynb
│  ├─ 05_cluster14_vs_15_intake.ipynb
│  ├─ 06_intake_vs_completed_distribution.ipynb
│  └─ 07_spatial_patterns.ipynb
└─ outputs/
├─ figures/
└─ tables/
```

## Analysis Flow

### 1. Data Inventory
Review raw CAISO files, enumerate available attributes, and document structural limitations (e.g. lack of stable project IDs across time).

### 2. Cleaning & Canonicalization
Normalize:
- project identifiers,
- technology labels,
- MW values,
- status definitions, and
- location fields (county, PTO, POI, voltage).

Output clean, reusable tables to `data/processed/`.

### 3. Cohort Survivability (Cluster 15)
Analyze attrition patterns by:
- technology,
- project size (MW buckets),
- withdrawal timing (early vs later exits).

Results are evaluated using both **project counts** and **MW-weighted measures**.

### 4. Intake Evolution (Cluster 14 vs 15)
Compare how the **nature of proposed projects** has changed over time, including:
- MW distribution,
- technology mix,
- grid-context attributes where available.

This analysis focuses on **intake behavior**, not outcomes for Cluster 14.

### 5. Intake vs Historical Completion Mismatch
Compare:
- Cluster 14 intake,
- Cluster 15 cohort,
- pooled historical completed projects,

to identify **structural mismatches** between what is proposed and what historically completes.

### 6. Spatial Patterns
Using county-level geography:
- map withdrawal rates,
- map total proposed MW,
- visualize scale vs attrition patterns.

County aggregation is used because **public queue data does not include project or substation coordinates**.

---

## Key Findings (High-Level)

Across the analyses:

- **Withdrawal is the dominant outcome** in the CAISO interconnection process.
- **Attrition is front-loaded**: many withdrawals occur relatively soon after queue entry.
- **Project scale matters**:
  - Large projects dominate proposed MW and exhibit materially lower withdrawal rates.
- **Technology effects are conditional on scale** rather than standalone drivers.
- **Intake composition differs from historical completions**, suggesting structural misalignment between what enters the queue and what ultimately succeeds.
- Geographic patterns indicate **regional clustering** of both proposals and attrition, though precision is limited by public data granularity.

These results point to survivability being driven by **feasibility, scale, and economic robustness**, not any single attribute.

---

## Reproducibility

All results can be reproduced by:

```bash
python -m venv .venv
source .venv/bin/activate   # or .venv\Scripts\activate on Windows
pip install -r requirements.txt
````

Then run notebooks sequentially from `01` → `07`.

## Limitations

* Public CAISO data does **not** support per-project longitudinal tracking.
* POI names are provided without coordinates, limiting spatial precision.
* Completed projects are pooled across cohorts and years.
* Results reflect **observed status at time of publication**, not future outcomes.

These limitations are structural and explicitly documented rather than obscured.

## Roadmap & Extensions

The current analysis largely exhausts **survivability insights available from public queue snapshots**.

Logical next directions include:

* building a **repeatable ingestion framework** for new clusters,
* incorporating **POI or substation GIS data** to enable node-level risk analysis,
* extending the canonical pipeline to **other ISOs** (e.g., PJM, MISO) for comparison,
* or integrating **network upgrade and cost exposure** where public data allows.

## Disclaimer

This project uses only **publicly available CAISO data** and is intended for educational and analytical purposes. All interpretations are the author’s own and do not represent CAISO or any affiliated institution.
