# student_engagement_assigment

This project builds an end-to-end data pipeline using Python and Pandas based on the Medallion architecture (Bronze → Silver → Gold) to analyze student engagement.

## 📁 Folder Structure

```text
student_engagement_assigment/
├── data/
│   ├── raw/                   # Raw CSV files (Bronze Layer)
│   ├── cleaned/               # Cleaned data (Silver Layer)
│   └── transformed/           # Final features & aggregations (Gold Layer)
│
├── scripts/
│   ├── ingest_data.py         # Load CSVs into (Bronze layer)
│   ├── clean_data.py          # Clean & normalize (Silver layer)
│   ├── transform_data.py      # Aggregations, joins (Gold layer)
│   └── visualize.py           # Visualizations
│
├── outputs/
│   └── visualizations/        # Charts, graphs, etc.
│
├── diagrams/
│   └── data_flow_diagram.png  # Medallion architecture overview
│
├── README.md                  # Project overview and instructions
└── requirements.txt           # Python dependencies


## How to Run

1. Install dependencies:
```bash
pip install -r requirements.txt
```

2. Run the pipeline scripts in order:
```bash
python scripts/ingest_data.py
python scripts/clean_data.py
python scripts/transform_data.py
python scripts/visualize.py
```