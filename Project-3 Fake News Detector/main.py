import os
import re
import joblib
import pandas as pd
import nltk

from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score, classification_report

nltk.download("punkt", quiet=True)
nltk.download("stopwords", quiet=True)

DATASET = "news.csv"
MODEL = "fake_news_model.pkl"
VECTORIZER = "tfidf_vectorizer.pkl"

df = None
accuracy = None
report = None

stop_words = set(stopwords.words("english"))

def line():
    print("="*60)

def load_dataset():
    global df
    try:
        df = pd.read_csv(DATASET)
        if df.empty:
            print("Dataset is empty.")
            return False
        return True
    except FileNotFoundError:
        print("Dataset not found.")
    except Exception as e:
        print("Error:", e)
    return False

def view_data():
    if load_dataset():
        line(); print(df.to_string(index=False)); line()

def analyze_data():
    if not load_dataset(): return
    line()
    print("DATA ANALYSIS")
    line()
    print("Total Records     :", len(df))
    print("Fake News         :", (df["label"]=="FAKE").sum())
    print("Real News         :", (df["label"]=="REAL").sum())
    print("Missing Values    :", df.isnull().sum().sum())
    print("Duplicate Records :", df.duplicated().sum())
    print("Dataset Shape     :", df.shape)
    line()

def preprocess(text):
    text = str(text).lower()
    text = re.sub(r"[^a-zA-Z\s]"," ",text)
    words = word_tokenize(text)
    words = [w for w in words if w not in stop_words]
    return " ".join(words)

def train_model():
    global accuracy, report
    if not load_dataset(): return
    try:
        temp=df.copy()
        temp["clean"]=temp["text"].apply(preprocess)
        vec=TfidfVectorizer(max_features=5000)
        X=vec.fit_transform(temp["clean"])
        y=temp["label"]
        X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.2,random_state=42)
        model=MultinomialNB()
        model.fit(X_train,y_train)
        pred=model.predict(X_test)
        accuracy=accuracy_score(y_test,pred)
        report=classification_report(y_test,pred)
        joblib.dump(model,MODEL)
        joblib.dump(vec,VECTORIZER)
        print(f"Model trained successfully.\nAccuracy: {accuracy*100:.2f}%")
    except Exception as e:
        print("Training Error:",e)

def predict_news():
    try:
        if not(os.path.exists(MODEL) and os.path.exists(VECTORIZER)):
            print("Please train the model first.")
            return
        news=input("Enter News:\n").strip()
        if not news:
            print("News cannot be empty.")
            return
        model=joblib.load(MODEL)
        vec=joblib.load(VECTORIZER)
        clean=preprocess(news)
        X=vec.transform([clean])
        pred=model.predict(X)[0]
        conf=max(model.predict_proba(X)[0])*100
        print("\nPrediction :",pred)
        print(f"Confidence : {conf:.2f}%")
    except Exception as e:
        print("Prediction Error:",e)

def view_accuracy():
    global accuracy, report
    try:
        if accuracy is None:
            print("Train the model first.")
            return
        line()
        print(f"Accuracy : {accuracy*100:.2f}%")
        line()
        print(report)
    except Exception as e:
        print("Error:",e)

def menu():
    while True:
        line()
        print(" AI Based Fake News Detection Tool ")
        line()
        print("1. View Data")
        print("2. Analyze Data")
        print("3. Train Model")
        print("4. Predict News")
        print("5. View Accuracy")
        print("6. Exit")
        line()
        try:
            ch=int(input("Enter Choice: "))
            if ch==1: view_data()
            elif ch==2: analyze_data()
            elif ch==3: train_model()
            elif ch==4: predict_news()
            elif ch==5: view_accuracy()
            elif ch==6:
                line()
                print("Thank You for Using")
                print("AI Based Fake News Detection Tool")
                line()
                break
            else:
                print("Please enter a choice between 1 and 6.")
        except ValueError:
            print("Invalid input. Please enter a number.")
        except Exception as e:
            print("Unexpected Error:",e)

if __name__=="__main__":
    menu()
