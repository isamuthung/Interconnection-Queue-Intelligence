# CAISO Interconnection Queue Survivability Analysis

## Overview

This repository contains a focused, reproducible data analytics project examining **survivability and attrition in the CAISO interconnection queue** using only **publicly available disclosures**. The objective is to understand **which types of generation projects persist or withdraw**, *when* withdrawals tend to occur, and *how project characteristics relate to interconnection risk*.

The project emphasizes **interpretability, clean data pipelines, and transparency** rather than complex modeling. It is designed as an applied analysis demonstrating practical skills in **energy systems understanding**, **data cleaning**, and **exploratory survivability analysis**.

## Motivation

Interconnection queues are one of the most significant bottlenecks to clean energy deployment in the United States. In CAISO, hundreds of generation and storage projects enter the queue, yet **a large majority never reach completion**.

While CAISO publishes queue data, it is provided as **static snapshots**, fragmented across multiple files, and not structured for analysis. This project reorganizes those disclosures into analysis-ready datasets and uses them to identify **systematic patterns of attrition and persistence** that are not obvious from raw reports.

## Scope and Design Philosophy

This analysis is **retrospective and descriptive**, not predictive.

It focuses on:

* **Observed outcomes** (active vs withdrawn vs completed)
* **Structural patterns**, not individual project forecasting
* **Clear assumptions and limitations**, rather than black-box models

Out of scope by design:

* Full longitudinal tracking of individual projects
* Internal CAISO review stages or restudies
* Market Participant Portal or non-public data
* Machine-learning or predictive risk scoring
  
## Data Sources

The project uses exactly **two public CAISO Excel files**:

1. **Public Queue Report** (`publicqueuereport.xlsx`)
   A system-wide snapshot of active, withdrawn, and completed interconnection requests.

2. **Cluster 15 Interconnection Requests** (`cluster-15-interconnection-requests.xlsx`)
   A single intake cohort with consistent rules, enabling clean cohort-level analysis.

No scraping, APIs, or restricted portals are used.

## Repository Structure

```
├─ README.md
├─ requirements.txt
├─ data/
│  ├─ raw/        # Original CAISO XLSX files (unchanged)
│  └─ processed/  # Cleaned, analysis-ready tables
├─ notebooks/
│  ├─ 01_data_inventory.ipynb
│  ├─ 02_clean_public_queue.ipynb
│  ├─ 03_clean_cluster15.ipynb
│  └─ 04_survivability_insights.ipynb
└─ outputs/
   ├─ figures/
   └─ tables/
```

## Analysis Approach

The analysis proceeds in four steps:

1. **Data Inventory**
   Inspect raw CAISO files, identify usable fields, and document structural limitations (e.g., lack of full project timelines).

2. **Cleaning & Standardization**
   Normalize project identifiers, technology labels, MW values, and status categories. Produce consistent, analysis-ready tables.

3. **Cohort Survivability Analysis (Cluster 15)**
   Examine outcomes by:

   * technology category
   * project size (MW buckets)
   * withdrawal timing (early vs late exits)

   Both project counts and MW-weighted results are evaluated.

4. **Interpretation**
   Translate observed patterns into structural insights about interconnection risk while clearly stating what the data does *not* support.

## Key Findings

From the Public Queue and Cluster 15 analysis:

* **Withdrawal is the dominant outcome** in the CAISO interconnection process; only a minority of projects remain active or reach completion.
* **Attrition is front-loaded**: a large share of withdrawn projects exit within the first year after queue entry.
* **Project size matters**:

  * Large projects (≥100 MW) dominate Cluster 15 and exhibit **substantially lower withdrawal rates** than smaller projects.
  * Small projects show higher apparent attrition, though sample sizes are limited.
* **Technology matters**, but interacts with scale:

  * Survivability differences are most pronounced when technology is examined **conditional on project size** rather than in isolation.

Overall, interconnection survivability appears to be driven less by any single attribute and more by a combination of **scale, feasibility, and early economic viability**.

## Skills Demonstrated

This project demonstrates:

* **Data analytics**

  * Cleaning and restructuring real-world, imperfect datasets
  * Designing reproducible analysis pipelines
  * Producing interpretable tables and visualizations

* **Energy systems literacy**

  * Understanding ISO interconnection processes
  * Framing analytics around grid constraints and queue dynamics
  * Interpreting results in a policy-relevant context

* **Technical practice**

  * Python (pandas, numpy, matplotlib)
  * Jupyter notebooks with narrative structure
  * Reproducible project organization and environment setup

## Reproducibility

All results can be reproduced by:

1. Creating a Python virtual environment
2. Installing dependencies from `requirements.txt`
3. Running notebooks sequentially from `01` → `04`

No external services or credentials are required.

## Limitations

* The analysis is constrained to **public snapshot data** and cannot reconstruct full per-project histories.
* Some attributes (e.g. storage MWh for Cluster 15) are unavailable in the public export.
* Active projects may withdraw in the future; results reflect observed states at time of publication.


## Disclaimer

This project uses only **publicly available CAISO data** and is intended for educational and analytical purposes. Interpretations are the author’s own and do not represent CAISO or any affiliated organization.

---
