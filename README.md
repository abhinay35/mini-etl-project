# Mini ETL Project (Python + SQLite)

## 📌 Project Overview
This project demonstrates a simple ETL (Extract, Transform, Load) pipeline using Python.  
It processes sales data, performs cleaning and transformation, and stores the results in a SQLite database.

---

## ⚙️ Tech Stack
- Python
- Pandas
- SQLite

---

## 🔄 ETL Process

### 1. Extract
- Read raw data from CSV file

### 2. Transform
- Removed duplicates
- Handled missing values
- Created new column: `total_price`
- Added `category` column

### 3. Load
- Loaded cleaned data into SQLite database

---

## 📂 Project Structure
mini-etl-project/
│
├── data/
│ └── sales.csv
│
├── scripts/
│ └── etl.py
│
├── output/
│ └── sales.db
│
└── README.md

---

## ▶️ How to Run

#bash
pip install pandas
cd scripts
python etl.py

✅ Output
Processed data stored in SQLite database (sales.db)
