# AI Helpdesk Chatbot

## Overview

AI Helpdesk Chatbot is a Python-based conversational AI application designed to answer frequently asked employee queries. The chatbot uses Natural Language Processing (NLP) techniques such as tokenization, stopword removal, and keyword-based matching to provide relevant responses from a predefined FAQ dataset.


---

## Features

* View FAQ Dataset
* Question-Answer Chatbot
* NLP-Based Text Processing
* Tokenization & Stopword Removal
* Keyword Matching
* Confidence Score Calculation
* Add New FAQs
* Dataset Analysis
* Flask Web Application
* Menu-Driven Interface

---

## Technologies Used

* Python
* Pandas
* NLTK
* Flask

---

## Project Structure

```text
AI_Internal_Helpdesk_Chatbot/
│
├── faq_dataset.csv
├── main.py
├── app.py
├── requirements.txt
└── README.md
```

---

## Installation

Install the required libraries:

```bash
pip install -r requirements.txt
```

---

## Run the Chatbot

```bash
python main.py
```

---

## Run the Flask Application

```bash
python app.py
```

Open your browser and visit:

```text
http://127.0.0.1:5000
```

---

## Sample Output

```text
====== AI INTERNAL HELPDESK CHATBOT ======

1. View FAQ Dataset
2. Chat With Bot
3. Add FAQ
4. Analyze Data
5. Exit

Enter Choice: 2

You: what is payday

Bot: Salary is credited on the last working day.
Confidence: 100.0 %
```

---

## Project Workflow

1. Load the FAQ dataset.
2. Preprocess text using NLTK.
3. Tokenize user input.
4. Remove stopwords.
5. Compare user keywords with FAQ questions.
6. Find the best matching question.
7. Display the corresponding answer.

---

## Learning Outcomes

* Natural Language Processing (NLP)
* Tokenization
* Stopword Removal
* Text Preprocessing
* Keyword Matching
* Conversational AI
* Dataset Management
---



