# Nyansapo Baseline Schools Performance Report Generation

## Overview

This project provides a comprehensive Python-based tool for generating detailed school performance reports based on student literacy and numeracy assessments.

## 🔒 Security Considerations

- Input validation for CSV files
- Error handling to prevent exposure of sensitive student data
- Minimal external dependencies
- Use of `pd.to_numeric(errors='coerce')` to safely handle numeric conversions
- Explicit data cleaning and standardization processes

## Prerequisites

- Python 3.8+
- Virtual Environment (recommended)

## Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/school-performance-reports.git
cd school-performance-reports
```

### 2. Create Virtual Environment

```bash
# For Unix/macOS
python3 -m venv venv
source venv/bin/activate

# For Windows
python -m venv venv
.\venv\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

#### requirements.txt

```
pandas==2.1.4
python-docx==1.1.0
matplotlib==3.8.2
numpy==1.26.3
```

## Project Structure

```
school-performance-reports/
│
├── data/                  # Raw CSV input files
├── summary/               # Generated summary CSV files
├── reports-docs/          # Generated Word document reports
│
├── generate_summaries.py  # Data processing and summary generation
├── generate_reports.py    # Report generation from summaries
└── README.md
```

## Script Details

### 1. generate_summaries.py

#### Purpose

Processes raw student assessment data and generates standardized summary files.

#### Key Features

- Data cleaning and normalization
- Extraction of literacy and numeracy levels
- Error handling for various input scenarios

#### Workflow

1. Reads CSV files from `data/` directory
2. Cleans and standardizes data
3. Categorizes students' literacy and numeracy levels
4. Generates summary files in `summary/` directory

#### Security Measures

- Uses `pd.to_numeric(errors='coerce')` for safe numeric conversion
- Removes unnecessary columns
- Standardizes gender representation
- Handles missing or invalid data gracefully

### 2. generate_reports.py

#### Purpose

Generates comprehensive Word document reports from summary CSV files.

#### Key Features

- Automated report generation
- Performance categorization
- Percentage calculations
- Embedded recommendations
- Optional performance graph integration

#### Workflow

1. Reads summary files from `summary/` directory
2. Calculates performance percentages
3. Creates detailed Word documents
4. Saves reports in `reports-docs/` directory

#### Security Measures

- Validates file paths before processing
- Uses `os.makedirs(exist_ok=True)` for safe directory creation
- Handles scenarios with missing summary or graph files

## Usage

### Generate Summaries

```bash
python generate_summaries.py
```

### Generate graphs

```bash
python generate_graphs.py
```

### Generate Reports

```bash
python generate_reports.py
```

## Dependencies

- **pandas**: Data manipulation
- **python-docx**: Word document generation
- **matplotlib**: Optional graphing
- **numpy**: Numerical computations
