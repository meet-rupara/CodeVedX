# ==========================================
# STUDENT PERFORMANCE PREDICTION SYSTEM
# ==========================================

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score


# Global dataframe
df = None


# ==========================================
# GENERATE DATASET
# ==========================================

def generate_dataset():

    global df

    np.random.seed(42)

    n = 200

    attendance = np.random.randint(50, 100, n)
    study = np.random.randint(1, 9, n)
    internal = np.random.randint(40, 100, n)
    assignment = np.random.randint(45, 100, n)
    previous = np.random.randint(40, 95, n)

    final = (
        attendance * 0.20 +
        study * 3 +
        internal * 0.25 +
        assignment * 0.20 +
        previous * 0.25 +
        np.random.randint(-5, 6, n)
    )

    final = np.clip(final, 35, 100)

    df = pd.DataFrame({
        "Attendance": attendance,
        "StudyHours": study,
        "InternalMarks": internal,
        "Assignment": assignment,
        "PreviousMarks": previous,
        "FinalScore": final.round(1)
    })

    df.to_csv("student_data.csv", index=False)

    print("\nDataset generated successfully.")
    print("200 student records created.")


# ==========================================
# LOAD DATASET
# ==========================================

def load_dataset():

    global df

    try:
        df = pd.read_csv("student_data.csv")
        return True

    except:
        print("\nDataset not found.")
        print("Please generate the dataset first.")
        return False


# ==========================================
# VIEW DATASET
# ==========================================

def view_dataset():

    if load_dataset():
        print("\nFirst 10 Records:\n")
        print(df.head(10))


# ==========================================
# ANALYZE DATASET
# ==========================================

def analyze_dataset():

    if load_dataset():

        print("\nDataset Shape:")
        print(df.shape)

        print("\nData Types:")
        print(df.dtypes)

        print("\nStatistical Summary:")
        print(df.describe())

        print("\nFeature Selection:")
        print(df.columns)


# ==========================================
# HANDLE MISSING VALUES
# ==========================================

def handle_missing_values():

    global df

    if load_dataset():

        print("\nMissing Values:\n")
        print(df.isnull().sum())

        df.fillna(df.mean(numeric_only=True),
                  inplace=True)

        df.to_csv("student_data.csv",
                  index=False)

        print("\nMissing values handled.")


# ==========================================
# VISUALIZE DATA
# ==========================================

def visualize_data():

    if load_dataset():

        plt.figure(figsize=(8,6))
        sns.heatmap(df.corr(),
                    annot=True,
                    cmap="Blues")
        plt.title("Correlation Heatmap")
        plt.show()

        plt.figure(figsize=(6,4))
        plt.hist(df["Attendance"],
                 bins=10)
        plt.xlabel("Attendance")
        plt.ylabel("Students")
        plt.title("Attendance Distribution")
        plt.show()

        plt.figure(figsize=(6,4))
        plt.scatter(df["StudyHours"],
                    df["FinalScore"])
        plt.xlabel("Study Hours")
        plt.ylabel("Final Score")
        plt.title("Study Hours vs Final Score")
        plt.show()


# ==========================================
# PREDICT PERFORMANCE
# ==========================================
def predict_performance():

    if load_dataset():

        # Feature Selection
        X = df[
            [
                "Attendance",
                "StudyHours",
                "InternalMarks",
                "Assignment",
                "PreviousMarks"
            ]
        ]

        y = df["FinalScore"]

        # Train-Test Split
        X_train, X_test, y_train, y_test = train_test_split(
            X,
            y,
            test_size=0.2,
            random_state=42
        )

        # Model Training
        model = LinearRegression()
        model.fit(X_train, y_train)

        # Model Evaluation
        prediction = model.predict(X_test)
        accuracy = r2_score(y_test, prediction)

        print(f"\nModel Accuracy: {accuracy * 100:.2f}%")

        print("\nEnter Student Details:")

        attendance = float(input("Attendance (%): "))
        study = float(input("Study Hours: "))
        internal = float(input("Internal Marks: "))
        assignment = float(input("Assignment Marks: "))
        previous = float(input("Previous Marks: "))

        # Create DataFrame with correct feature names
        student = pd.DataFrame({
            "Attendance": [attendance],
            "StudyHours": [study],
            "InternalMarks": [internal],
            "Assignment": [assignment],
            "PreviousMarks": [previous]
        })

        # Prediction
        result = model.predict(student)

        print(f"\nPredicted Final Score: {result[0]:.2f}")
# ==========================================
# MAIN MENU
# ==========================================

while True:

    print("\n------- Student Performance Prediction System -------")
    print("1. Generate Dataset")
    print("2. View Dataset")
    print("3. Analyze Dataset")
    print("4. Handle Missing Values")
    print("5. Visualize Data")
    print("6. Predict Performance")
    print("7. Exit")

    try:

        choice = int(
            input("\nEnter your choice: ")
        )

        if choice == 1:
            generate_dataset()

        elif choice == 2:
            view_dataset()

        elif choice == 3:
            analyze_dataset()

        elif choice == 4:
            handle_missing_values()

        elif choice == 5:
            visualize_data()

        elif choice == 6:
            predict_performance()

        elif choice == 7:
            print("\nThank you.")
            break

        else:
            print("\nInvalid choice.")

    except ValueError:
        print("\nPlease enter a valid number.")