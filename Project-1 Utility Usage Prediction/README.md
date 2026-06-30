# Utility Usage Prediction System

## Overview

The Utility Usage Prediction System is a Machine Learning application developed using Python. It predicts household utility usage (kWh) based on the number of household members and their average daily usage hours.

The project uses the Linear Regression algorithm from Scikit-learn and provides a simple menu-driven interface for managing data, training the model, and making predictions.

---

## Features

- View Dataset
- Add New Data
- Update Existing Data
- Train Machine Learning Model
- Predict Utility Usage
- Automatic Model Saving
- Exception Handling
- Menu Driven Interface

---

## Technologies Used

- Python
- Pandas
- Scikit-learn
- Joblib

---

## Project Structure

```
Project-1-Utility-Prediction/
│
├── main.py
├── utility_usage.csv
├── requirements.txt
└── README.md
```

## Dataset

The dataset contains the following columns:

| Column | Description |
|---------|-------------|
| Members | Usage_Hours_Per_Day | Utility_Usage_kWh |

Example:

Members | Usage Hours | Utility Usage
-------- | ----------- | -------------
4 | 6 | 240
2 | 3 | 115
5 | 8 | 335

---

## Machine Learning Algorithm

- Linear Regression

Features:
- Members
- Usage_Hours_Per_Day

Target:
- Utility_Usage_kWh

---

## Installation

Install the required libraries:

```bash
pip install -r requirements.txt
```

---

## Run the Project

```bash
python main.py
```

---

## Menu

```
===== Utility Usage Prediction =====

1. View Dataset
2. Add Data
3. Update Data
4. Train Model
5. Predict Utility Usage
6. Exit
```

---

## Project Workflow

1. Load Dataset
2. View/Add/Update Data
3. Train Linear Regression Model
4. Save Model
5. Predict Utility Usage

---

## Exception Handling

The application handles:

- Missing dataset
- Missing model file
- Invalid row number
- Invalid user input
- Prediction errors

---

## Future Enhancements

- Random Forest Regression
- Decision Tree Regression
- Model Accuracy Comparison
- Graphical User Interface
- Data Visualization
- Delete Record Option

---

