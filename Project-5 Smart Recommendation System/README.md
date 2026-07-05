# 🎯 Smart Recommendation System

## Overview

The **Smart Recommendation System** is a Machine Learning application developed using **Python** that recommends similar items based on their characteristics. The system uses **TF-IDF (Term Frequency-Inverse Document Frequency)** for feature extraction and **Cosine Similarity** to identify and rank the most relevant recommendations.

Users can browse the dataset, search for items, add new entries, and receive personalized recommendations based on content similarity.

---

## Features

- 📋 View all items in the dataset
- 🔍 Search items by title
- ➕ Add new items to the dataset
- 🤖 Content-Based Recommendation System
- 📊 TF-IDF Feature Extraction
- 📐 Cosine Similarity Ranking
- 📈 Dataset statistics
- 💾 Automatic CSV data storage
- 🖥️ User-friendly console interface

---

## Machine Learning Concepts Used

- Content-Based Filtering
- TF-IDF Vectorization
- Cosine Similarity
- Feature Engineering
- Text Preprocessing
- Similarity Scoring

---

## Technologies Used

- Python
- Pandas
- NumPy
- Scikit-learn

---

## Project Structure

```
Smart-Recommendation-System/
│
├── main.py
├── dataset.csv
├── requirements.txt
├── README.md
└── screenshots/
```

---

## Dataset

The dataset contains various entertainment items including:

- Movies
- Anime
- TV Series
- Books
- Games

Each record contains:

| Column | Description |
|---------|-------------|
| ID | Unique identifier |
| Title | Item name |
| Genre | Genre of the item |
| Language | Original language |
| Category | Movie, Anime, Book, Series, Game |
| Rating | User/IMDb rating |

---

## Recommendation Workflow

```
User selects an item
        │
        ▼
Load Dataset
        │
        ▼
Combine Features
(Genre + Language + Category)
        │
        ▼
TF-IDF Vectorization
        │
        ▼
Cosine Similarity Calculation
        │
        ▼
Rank Similar Items
        │
        ▼
Display Top 5 Recommendations
```

---

## Installation

### 1. Clone the repository

```bash
git clone https://github.com/yourusername/Smart-Recommendation-System.git
```

### 2. Navigate to the project folder

```bash
cd Smart-Recommendation-System
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the project

```bash
python main.py
```

---

## Sample Menu

```
====================================
 SMART RECOMMENDATION SYSTEM
====================================

1. View All Items
2. Search Item
3. Add New Item
4. Get Recommendations
5. Dataset Statistics
6. Exit
```

---

## Example Recommendation

```
Enter Item Title:
Interstellar

Top 5 Recommendations

1. Inception
Similarity : 91.82%

2. The Martian
Similarity : 88.64%

3. Arrival
Similarity : 85.13%

4. Gravity
Similarity : 82.47%

5. Ad Astra
Similarity : 79.91%
```

---

## Libraries Used

- pandas
- numpy
- scikit-learn

---

## Future Improvements

- User profiles
- Personalized recommendations
- Hybrid recommendation system
- Collaborative filtering
- Deep Learning-based recommendations
- Movie posters and images
- GUI using Tkinter or Streamlit
- Web application using Flask or Django
- Larger dataset
- Recommendation evaluation metrics

---

## Learning Outcomes

This project demonstrates practical implementation of:

- Machine Learning
- Recommendation Systems
- Natural Language Processing (NLP)
- Feature Engineering
- TF-IDF Vectorization
- Cosine Similarity
- Data Processing with Pandas
- Python Programming

---
