# AI Based Fake News Detection Tool

## Overview

The **AI Based Fake News Detection Tool** is a Machine Learning project developed using **Python** and **Natural Language Processing (NLP)**. It classifies news articles as **FAKE** or **REAL** based on their content and provides a confidence score for each prediction.

The project uses **TF-IDF Vectorization** for feature extraction and the **Multinomial Naive Bayes** algorithm for text classification. The trained model is saved locally, allowing predictions without retraining every time.

---

## Features

* View dataset
* Analyze dataset
* Train Machine Learning model
* Predict whether news is **FAKE** or **REAL**
* Display prediction confidence score
* View model accuracy
* Save and load trained model
* Simple menu-driven console application
* Exception handling for smooth execution

---

## Technologies Used

* Python
* Pandas
* NumPy
* Scikit-learn
* NLTK
* Joblib

---

## NLP Techniques Used

* Text Preprocessing
* Tokenization
* Stopword Removal
* TF-IDF Vectorization

---

## Machine Learning Algorithm

* Multinomial Naive Bayes

---

## Project Structure

```text
AI-Based-Fake-News-Detection/
│
├── main.py
├── news.csv
├── requirements.txt
├── README.md

```

---

## Installation

Install the required libraries:

```bash
pip install -r requirements.txt
```

---

## How to Run

Run the project using:

```bash
python main.py
```

---

## Menu Options

1. View Data
2. Analyze Data
3. Train Model
4. Predict News
5. View Accuracy
6. Exit

---

## Sample Output

```text
============================================
      AI Based Fake News Detection Tool
============================================

1. View Data
2. Analyze Data
3. Train Model
4. Predict News
5. View Accuracy
6. Exit
```

Example Prediction:

```text
Enter News:

Scientists discover a new species of marine life.

Prediction : REAL

Confidence : 97.84%
```

---

## Future Improvements

* Larger dataset for improved accuracy
* Graphical User Interface (GUI)
* Flask or Django web application
* Deep Learning models such as LSTM or BERT
* Live news API integration

---

