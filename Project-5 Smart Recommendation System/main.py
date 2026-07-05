import os
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

DATASET_FILE = "dataset.csv"
df = None

def load_dataset():
    global df
    if not os.path.exists(DATASET_FILE):
        print("\nDataset not found!")
        return False
    try:
        df = pd.read_csv(DATASET_FILE)
        return True
    except Exception as e:
        print(f"\nError loading dataset: {e}")
        return False

def view_items():
    if load_dataset():
        print("\n========== ALL ITEMS ==========\n")
        print(df.to_string(index=False))

def search_item():
    if load_dataset():
        keyword = input("\nEnter title to search: ").strip().lower()
        result = df[df["Title"].str.lower().str.contains(keyword, na=False)]
        if result.empty:
            print("\nNo matching item found.")
        else:
            print(result.to_string(index=False))

def add_item():
    if not load_dataset():
        return
    print("\n====== ADD NEW ITEM ======")
    title=input("Title: ").strip()
    genre=input("Genre: ").strip()
    language=input("Language: ").strip()
    category=input("Category: ").strip()
    while True:
        try:
            rating=float(input("Rating (0-10): "))
            if 0<=rating<=10:
                break
        except:
            pass
        print("Invalid rating.")
    new_id = 1 if df.empty else int(df["ID"].max())+1
    new = pd.DataFrame({
        "ID":[new_id],"Title":[title],"Genre":[genre],
        "Language":[language],"Category":[category],"Rating":[rating]
    })
    pd.concat([df,new],ignore_index=True).to_csv(DATASET_FILE,index=False)
    print("\nItem added successfully.")

def recommend():
    if not load_dataset():
        return
    print("\n========== SMART RECOMMENDATION ENGINE ==========")
    title=input("\nEnter Item Title: ").strip()
    if title.lower() not in df["Title"].str.lower().values:
        print("Item not found.")
        return
    features=(df["Genre"].fillna("")+" "+
              df["Language"].fillna("")+" "+
              df["Category"].fillna(""))
    tfidf=TfidfVectorizer(stop_words="english")
    matrix=tfidf.fit_transform(features)
    sim=cosine_similarity(matrix)
    idx=df[df["Title"].str.lower()==title.lower()].index[0]
    scores=sorted(list(enumerate(sim[idx])),key=lambda x:x[1],reverse=True)
    print("\nTop 5 Recommendations\n")
    c=0
    for i,s in scores:
        if i==idx:
            continue
        row=df.iloc[i]
        print(f"{c+1}. {row['Title']}")
        print(f"   Genre      : {row['Genre']}")
        print(f"   Category   : {row['Category']}")
        print(f"   Language   : {row['Language']}")
        print(f"   Rating     : {row['Rating']}")
        print(f"   Similarity : {s*100:.2f}%\n")
        c+=1
        if c==5:
            break

def statistics():
    if not load_dataset():
        return
    print("\n========== DATASET STATISTICS ==========")
    print(f"Total Items : {len(df)}")
    print(f"Average Rating : {df['Rating'].mean():.2f}")
    print("\nCategory Counts")
    print(df["Category"].value_counts())
    print("\nGenre Counts")
    print(df["Genre"].value_counts())
    print("\nLanguage Counts")
    print(df["Language"].value_counts())

def main():
    while True:
        print("\n====================================")
        print(" SMART RECOMMENDATION SYSTEM")
        print("====================================")
        print("1. View All Items")
        print("2. Search Item")
        print("3. Add New Item")
        print("4. Get Recommendations")
        print("5. Dataset Statistics")
        print("6. Exit")
        ch=input("\nEnter Choice: ").strip()
        if ch=="1":
            view_items()
        elif ch=="2":
            search_item()
        elif ch=="3":
            add_item()
        elif ch=="4":
            recommend()
        elif ch=="5":
            statistics()
        elif ch=="6":
            print("Thank you for using Smart Recommendation System.")
            break
        else:
            print("Invalid choice.")

if __name__=="__main__":
    main()
