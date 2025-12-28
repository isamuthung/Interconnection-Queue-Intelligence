# CAISO Interconnection Queue Survivability Analysis

## Overview

This repository contains a small, self-contained data analytics project focused on the **California Independent System Operator (CAISO)** interconnection queue. The goal is to use **publicly available queue disclosures** to analyze **which types of generation and storage projects tend to survive or withdraw** from the interconnection process, and why.

The project is intentionally scoped as an **AML-scale (Applied, Modular, Learnable)** analysis: it emphasizes clean data pipelines, transparent assumptions, and interpretable results over complex modeling. It is designed to demonstrate applied skills in **energy systems analysis**, **data cleaning**, and **exploratory survivability analysis**.

---

## Motivation & Problem Context

Across the U.S., interconnection queues have become a critical bottleneck for clean energy deployment. In CAISO, hundreds of generation and storage projects enter the queue each year, but historically **most projects withdraw before reaching commercial operation**.

While CAISO publishes queue reports, the data is:
- snapshot-based rather than longitudinal,
- fragmented across files and cohorts,
- not packaged for direct analytics.

This creates an opportunity to:
- structure raw queue disclosures into analysis-ready datasets,
- examine **patterns of attrition vs persistence**, and
- connect project characteristics (technology, size, storage duration) to outcomes.

---

## Project Scope

**This project focuses on:**
- Structural patterns, not prediction
- Retrospective survivability, not forecasting
- Transparency and reproducibility over black-box models

### In scope
- System-wide context using CAISO’s Public Queue Report
- Cohort-level analysis using Cluster 15 interconnection requests
- Comparisons of outcomes across:
  - technology types
  - project size
  - storage duration
- MW-weighted survivability (capacity that survives vs withdraws)

### Out of scope (by design)
- Full per-project historical timelines
- Internal CAISO review or restudy events
- Private or Market Participant Portal data
- Machine-learning prediction models

---

## Data Sources

This project uses **two public Excel files** from CAISO:

1. **Public Queue Report (`publicqueuereport.xlsx`)**  
   A system-wide snapshot listing active, withdrawn, and completed interconnection requests.

2. **Cluster 15 Interconnection Requests (`cluster-15-interconnection-requests.xlsx`)**  
   A single intake cohort with consistent submission rules and richer project attributes.

No private data, scraping, or restricted portals are used.

---

## Repository Structure

├─ README.md
├─ requirements.txt
├─ data/
│ ├─ raw/ # Original CAISO XLSX files (unchanged)
│ └─ processed/ # Cleaned, analysis-ready tables
├─ notebooks/
│ ├─ 01_data_inventory.ipynb
│ ├─ 02_clean_public_queue.ipynb
│ ├─ 03_clean_cluster15.ipynb
│ └─ 04_survivability_insights.ipynb
└─ outputs/
├─ figures/
└─ tables/


---

## Analysis Approach

1. **Data Inventory**
   - Inspect source files
   - Identify observable vs unobservable attributes
   - Document limitations explicitly

2. **Data Cleaning & Standardization**
   - Normalize project identifiers, technology categories, MW/MWh fields
   - Harmonize status labels (Active / Withdrawn / Completed)
   - Create analysis-ready tables

3. **Survivability Analysis**
   - Define outcomes as observed states (withdrawn, complete, active)
   - Compare survivability by:
     - technology type
     - project size buckets
     - storage duration
   - Produce both project-count and MW-weighted views

4. **Interpretation**
   - Highlight structural patterns
   - Connect findings to grid constraints and interconnection risk
   - Clearly state what the data can and cannot support

---

## Skills Demonstrated

This project demonstrates experience in:

### Data Analytics
- Working with imperfect, real-world energy datasets
- Cleaning and restructuring Excel-based disclosures
- Designing analysis pipelines with clear inputs and outputs
- Producing interpretable visualizations

### Energy Systems Literacy
- Understanding ISO/RTO interconnection processes
- Differentiating technologies and queue dynamics
- Framing analytics around grid and policy constraints

### Technical Practice
- Python (pandas, numpy, matplotlib)
- Jupyter notebooks with narrative structure
- Reproducible project organization
- Environment management with virtual environments

---

## Key Takeaways

The primary contribution of this project is **not a single metric**, but a method:
- transforming static queue snapshots into structured insights,
- revealing survivability patterns that are not obvious from raw reports, and
- highlighting data gaps that matter for clean-energy deployment.

This work can serve as a foundation for deeper studies involving:
- longitudinal snapshot tracking,
- inter-ISO comparisons,
- cost and upgrade risk modeling,
- or policy evaluation of queue reforms.

---

## Reproducibility

All results can be reproduced by:
1. Creating a Python virtual environment
2. Installing dependencies from `requirements.txt`
3. Running notebooks in order from `01` → `04`

No external APIs or private access keys are required.

---

## Disclaimer

This project uses only **publicly available CAISO information** and is intended for educational and analytical purposes. Interpretations are the author’s own and do not represent CAISO or any affiliated institution.
