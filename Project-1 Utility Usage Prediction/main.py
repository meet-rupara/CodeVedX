import os
import joblib
import pandas as pd
from sklearn.linear_model import LinearRegression

# ==========================
# File Names
# ==========================
DATA_FILE = "utility_usage.csv"
MODEL_FILE = "utility_usage_model.pkl"


# ==========================
# Dataset Functions
# ==========================



def view_data():
    try:
        df = pd.read_csv(DATA_FILE)

        if df.empty:
            print("\nDataset is empty.\n")
        else:
            print("\n========== DATASET ==========\n")
            print(df.reset_index())
            print()

    except FileNotFoundError:
        print("Dataset not found.")



def add_data():
    try:
        members = int(input("Members: "))
        hours = float(input("Usage Hours Per Day: "))
        usage = float(input("Utility Usage (kWh): "))

        df = pd.read_csv(DATA_FILE)

        new_row = pd.DataFrame({
            "Members": [members],
            "Usage_Hours_Per_Day": [hours],
            "Utility_Usage_kWh": [usage]
        })

        df = pd.concat([df, new_row], ignore_index=True)

        df.to_csv(DATA_FILE, index=False)

        print("\nData Added Successfully.")

    except Exception as e:
        print("Error:", e)


def update_data():
    try:

        df = pd.read_csv(DATA_FILE)

        if df.empty:
            print("Dataset is empty.")
            return

        print("\nCurrent Dataset\n")
        print(df.reset_index())

        row = int(input("\nEnter Row Number to Update: "))

        if row < 0 or row >= len(df):
            print("Invalid Row Number")
            return

        members = int(input("New Members: "))
        hours = float(input("New Usage Hours Per Day: "))
        usage = float(input("New Utility Usage (kWh): "))

        df.loc[row, "Members"] = members
        df.loc[row, "Usage_Hours_Per_Day"] = hours
        df.loc[row, "Utility_Usage_kWh"] = usage

        df.to_csv(DATA_FILE, index=False)

        print("\nRow Updated Successfully.")

    except Exception as e:
        print("Error:", e)


# ==========================
# Machine Learning
# ==========================

def train_model():
    try:

        df = pd.read_csv(DATA_FILE)

        if len(df) < 2:
            print("Not enough data to train.")
            return

        X = df[["Members", "Usage_Hours_Per_Day"]]
        y = df["Utility_Usage_kWh"]

        model = LinearRegression()
        model.fit(X, y)

        joblib.dump(model, MODEL_FILE)

        print("\nModel Trained Successfully.")

    except FileNotFoundError:
        print("Dataset not found.")

    except Exception as e:
        print("Training Error:", e)


def predict_usage():

    try:

        if not os.path.exists(MODEL_FILE):
            print("Train the model first.")
            return

        model = joblib.load(MODEL_FILE)

        members = int(input("Members: "))
        hours = float(input("Usage Hours Per Day: "))

        prediction = model.predict([[members, hours]])[0]

        print(
            "\nPredicted Utility Usage:",
            round(prediction, 2),
            "kWh"
        )

    except Exception as e:
        print("Prediction Error:", e)


# ==========================
# Main Program
# ==========================

def main():

   

    while True:

        print("\n===================================")
        print("UTILITY USAGE PREDICTION SYSTEM")
        print("===================================")

        print("1. View Dataset")
        print("2. Add Data")
        print("3. Update Data")
        print("4. Train Model")
        print("5. Predict Utility Usage")
        print("6. Exit")

        choice = input("\nEnter Choice: ")

        if choice == "1":
            view_data()

        elif choice == "2":
            add_data()

        elif choice == "3":
            update_data()

        elif choice == "4":
            train_model()

        elif choice == "5":
            predict_usage()

        elif choice == "6":
            print("\nThank You!")
            break

        else:
            print("\nInvalid Choice.")


# ==========================
# Run
# ==========================

if __name__ == "__main__":
    main()