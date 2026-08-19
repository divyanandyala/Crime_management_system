import pandas as pd
import matplotlib.pyplot as plt

FILE_NAME = "crimes.csv"


def load_data():
    try:
        df = pd.read_csv(FILE_NAME)
        return df
    except FileNotFoundError:
        print("Crime records file not found.")
        return None


def display_records():
    df = load_data()
    if df is not None:
        print("\n========== ALL CRIME RECORDS ==========")
        print(df)


def total_crimes():
    df = load_data()
    if df is not None:
        print("\nTotal Crime Records:", len(df))


def crime_type_analysis():
    df = load_data()
    if df is not None:
        data = df["Crime Type"].value_counts()
        print(data)
        data.plot(kind="bar")
        plt.title("Crime Type Analysis")
        plt.xlabel("Crime Type")
        plt.ylabel("Number of Crimes")
        plt.tight_layout()
        plt.show()


def status_analysis():
    df = load_data()
    if df is not None:
        data = df["Status"].value_counts()
        print(data)
        data.plot(kind="pie", autopct="%1.1f%%", startangle=90)
        plt.title("Solved vs Pending Cases")
        plt.ylabel("")
        plt.show()


def officer_analysis():
    df = load_data()
    if df is not None:
        data = df["Officer"].value_counts()
        print(data)
        data.plot(kind="bar")
        plt.title("Officer-wise Cases")
        plt.xlabel("Officer")
        plt.ylabel("Cases")
        plt.tight_layout()
        plt.show()


def location_analysis():
    df = load_data()
    if df is not None:
        data = df["Location"].value_counts()
        print(data)
        data.plot(kind="bar")
        plt.title("Location-wise Crime Analysis")
        plt.xlabel("Location")
        plt.ylabel("Cases")
        plt.tight_layout()
        plt.show()


def crime_analysis():
    while True:
        print("\n========== CRIME ANALYSIS ==========")
        print("1. Display All Crime Records")
        print("2. Total Crime Records")
        print("3. Crime Type Analysis")
        print("4. Case Status Analysis")
        print("5. Officer-wise Analysis")
        print("6. Location-wise Analysis")
        print("7. Back to Main Menu")

        choice = input("Enter Choice: ")

        if choice == "1":
            display_records()
        elif choice == "2":
            total_crimes()
        elif choice == "3":
            crime_type_analysis()
        elif choice == "4":
            status_analysis()
        elif choice == "5":
            officer_analysis()
        elif choice == "6":
            location_analysis()
        elif choice == "7":
            break
        else:
            print("Invalid Choice!")


if __name__ == "__main__":
    crime_analysis()