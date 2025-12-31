# CAISO Interconnection Queue Intelligence

## Overview

This repository contains a **reproducible, public-data analysis of the CAISO generator interconnection queue**, focused on **project survivability, attrition dynamics, intake composition, and spatial patterns**.

Using only **publicly available CAISO disclosures**, the project examines which types of projects tend to **withdraw versus persist**, **when attrition occurs**, how **intake composition differs across cohorts**, and how outcomes vary across **technology, scale, and geography**. The emphasis is on **interpretability, clean data pipelines, and methodological honesty**, rather than black-box prediction, producing insights that clarify **structural interconnection risk** while explicitly documenting the limits of public data.

## Motivation

Interconnection queues have become one of the largest bottlenecks to clean energy deployment in the United States. In CAISO, hundreds of generation and storage projects enter the queue each year, yet **a majority never reach completion**.

Although CAISO publishes queue data, it is released as **static snapshots**, fragmented across **multiple files and cohorts**, and not structured for longitudinal or comparative analysis. This project reorganizes those disclosures into **analysis-ready datasets** and uses them to surface **systematic patterns of attrition, persistence, and mismatch** that are not apparent in the raw queue reports.

## Scope & Design Philosophy

This project is **retrospective and descriptive**, not predictive.

### In Scope
- Observed outcomes (active / withdrawn / completed)
- Cohort-level survivability using Cluster 15
- Intake comparisons across Cluster 14 and Cluster 15
- Intake vs historical completion **distribution mismatch**
- County-level spatial patterns derived from public geography

### Explicitly Out of Scope (by Design)
- Per-project longitudinal tracking across years
- Internal CAISO study stages, re-studies, or cost assignments
- Market Participant Portal or any non-public data
- Machine-learning or predictive risk scoring

The guiding principle is **credible inference over over-reach**.

## Data Sources

The analysis uses **only public CAISO files**:

1. **Public Queue Report (`public_queue_report.xlsx`)**  
   A system-wide snapshot of active, withdrawn, and completed interconnection requests across all cohorts.

2. **Cluster 15 Interconnection Requests (`cluster15_interconnection_requests.xlsx`)**  
   A single, internally consistent intake cohort with richer project attributes, enabling clean survivability analysis.

3. **Preliminary Cluster 14 Project List (`preliminary_cluster14_project_list.xlsx`)**  
   A historical intake snapshot used to evaluate **how queue composition has changed over time**.

No APIs, scraping, or restricted portals are used.

## Repository Structure

```
├─ README.md
├─ requirements.txt
├─ data/
│ ├─ raw/ # Original CAISO XLSX and GIS files (unchanged)
│ └─ processed/ # Cleaned, canonical analysis tables and figures
├─ notebooks/
│ ├─ 01_data_management.ipynb
│ ├─ 02_clean_public_queue.ipynb
│ ├─ 03_clean_cluster15.ipynb
│ ├─ 04_clean_cluster14.ipynb
│ ├─ 05_survivability_analysis.ipynb
│ └─ 06_spatial_analysis.ipynb
├─ notebooks/
│ ├─ figures
│ ├─ tables

```

## Notebooks

The notebooks implement a **sequential, transparent analysis pipeline**: they begin by inventorying and inspecting raw CAISO files to document structural limitations, then clean and canonicalize the system-wide public queue and Cluster 14/15 intake datasets, producing standardized cohort-level tables. These cleaned datasets are used to analyze **survivability, attrition timing, scale and technology effects**, and to map **county-level spatial patterns** using public geographic boundaries, with each step explicitly scoped to what public data can reliably support.

## Key Findings (High-Level)

Across the analyses:

- **Withdrawal is the dominant outcome** in the CAISO interconnection process  
- **Attrition is front-loaded**, with many projects withdrawing relatively early after queue entry  
- **Project scale matters**: large projects dominate proposed MW and exhibit materially lower withdrawal rates  
- **Technology effects are conditional on scale**, rather than standalone drivers of survivability  
- **Intake composition differs from historical completions**, suggesting structural misalignment between what enters the queue and what ultimately succeeds  
- Spatial patterns indicate **regional clustering** of both proposals and attrition, though precision is constrained by public data granularity  

Together, these findings suggest survivability is driven by **feasibility, scale, and economic robustness**, not any single attribute.

## Reproducibility

All results can be reproduced by setting up a virtual environment and running the notebooks sequentially:

```
python -m venv .venv
source .venv/bin/activate   # or .venv\Scripts\activate on Windows
pip install -r requirements.txt
```
