import pandas as pd
import os
import nltk

nltk.download("punkt", quiet=True)
nltk.download("stopwords", quiet=True)

from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
CSV_FILE = os.path.join(BASE_DIR, "faq_dataset.csv")

stop_words = set(stopwords.words("english"))

def load_data():
    return pd.read_csv(CSV_FILE)

def view_data():
    data = load_data()
    print("\nFAQ Dataset:\n")
    print(data)

def add_faq():
    question = input("Enter Question: ").strip()
    answer = input("Enter Answer: ").strip()

    new_row = pd.DataFrame({
        "question": [question],
        "answer": [answer]
    })

    new_row.to_csv(
        CSV_FILE,
        mode="a",
        header=False,
        index=False
    )

    print("\nFAQ Added Successfully.")

def preprocess_text(text):
    tokens = word_tokenize(text.lower())

    filtered_words = []

    for word in tokens:
        if word.isalnum() and word not in stop_words:
            filtered_words.append(word)

    return set(filtered_words)

def chat_bot():
    data = load_data()

    user_question = input("\nYou: ").strip().lower()

    user_tokens = preprocess_text(user_question)

    best_match = None
    max_score = 0

    for i in range(len(data)):
        faq_question = data.loc[i, "question"]
        faq_tokens = preprocess_text(faq_question)

        score = len(user_tokens.intersection(faq_tokens))

        if score > max_score:
            max_score = score
            best_match = i

    if best_match is not None and max_score > 0:

        confidence = (
            max_score / max(len(user_tokens), 1)
        ) * 100

        print("\nBot:", data.loc[best_match, "answer"])
        print("Confidence:", round(confidence, 2), "%")

    else:
        print("\nBot: Sorry, I don't know the answer.")

def analyze_data():
    data = load_data()

    print("\nTotal FAQs:", len(data))

    words = " ".join(data["question"].astype(str))

    keyword_count = {}

    for word in words.lower().split():
        if word not in stop_words:
            keyword_count[word] = keyword_count.get(word, 0) + 1

    sorted_words = sorted(
        keyword_count.items(),
        key=lambda x: x[1],
        reverse=True
    )

    print("\nTop Keywords:\n")

    for word, count in sorted_words[:10]:
        print(word, ":", count)

while True:

    print("\n====== AI INTERNAL HELPDESK CHATBOT ======")
    print("1. View FAQ Dataset")
    print("2. Chat With Bot")
    print("3. Add FAQ")
    print("4. Analyze Data")
    print("5. Exit")

    choice = input("\nEnter Choice: ")

    if choice == "1":
        view_data()

    elif choice == "2":
        chat_bot()

    elif choice == "3":
        add_faq()

    elif choice == "4":
        analyze_data()

    elif choice == "5":
        print("Thank You.")
        break

    else:
        print("Invalid Choice.")
