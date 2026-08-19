import csv
import os

FILE_NAME = "crimes.csv"


# ============================================================
# CREATE CSV FILE
# ============================================================

def create_file():

    if not os.path.exists(FILE_NAME):

        with open(FILE_NAME, "w", newline="") as file:

            writer = csv.writer(file)

            writer.writerow([
                "Case ID",
                "Crime Type",
                "Location",
                "Date",
                "Officer",
                "Status"
            ])


# ============================================================
# ADD CRIME RECORD
# ============================================================

def add_crime():

    create_file()

    print("\n========== ADD CRIME RECORD ==========")

    case_id = input("Enter Case ID       : ")
    crime_type = input("Enter Crime Type    : ")
    location = input("Enter Location      : ")
    date = input("Enter Date (DD-MM-YYYY) : ")
    officer = input("Enter Officer Name  : ")
    status = input("Enter Status (Solved/Pending) : ")

    with open(FILE_NAME, "a", newline="") as file:

        writer = csv.writer(file)

        writer.writerow([
            case_id,
            crime_type,
            location,
            date,
            officer,
            status
        ])

    print("\nCrime Record Added Successfully!")


# ============================================================
# VIEW CRIME RECORDS
# ============================================================

def view_crimes():

    create_file()

    with open(FILE_NAME, "r") as file:

        reader = csv.DictReader(file)

        print("\n" + "=" * 100)
        print(" " * 40 + "CRIME RECORDS")
        print("=" * 100)

        print(
            f"{'Case ID':<10}"
            f"{'Crime Type':<20}"
            f"{'Location':<15}"
            f"{'Date':<15}"
            f"{'Officer':<20}"
            f"{'Status':<10}"
        )

        print("-" * 100)

        found = False

        for row in reader:

            found = True

            print(
                f"{row['Case ID']:<10}"
                f"{row['Crime Type']:<20}"
                f"{row['Location']:<15}"
                f"{row['Date']:<15}"
                f"{row['Officer']:<20}"
                f"{row['Status']:<10}"
            )

        if not found:
            print("No Crime Records Found.")

        print("=" * 100)


# ============================================================
# SEARCH CRIME
# ============================================================

def search_crime():

    create_file()

    case_id = input("\nEnter Case ID to Search : ")

    with open(FILE_NAME, "r") as file:

        reader = csv.DictReader(file)

        found = False

        for row in reader:

            if row["Case ID"] == case_id:

                print("\n========== CRIME RECORD FOUND ==========")

                print("Case ID    :", row["Case ID"])
                print("Crime Type :", row["Crime Type"])
                print("Location   :", row["Location"])
                print("Date       :", row["Date"])
                print("Officer    :", row["Officer"])
                print("Status     :", row["Status"])

                found = True
                break

        if not found:

            print("\nRecord Not Found.")


# ============================================================
# UPDATE CRIME
# ============================================================

def update_crime():

    create_file()

    case_id = input("\nEnter Case ID to Update : ")

    records = []
    found = False

    with open(FILE_NAME, "r") as file:

        reader = csv.DictReader(file)

        for row in reader:

            if row["Case ID"] == case_id:

                print("\nEnter New Details")

                row["Crime Type"] = input("New Crime Type : ")
                row["Location"] = input("New Location   : ")
                row["Date"] = input("New Date       : ")
                row["Officer"] = input("New Officer    : ")
                row["Status"] = input("New Status     : ")

                found = True

            records.append(row)

    if found:

        with open(FILE_NAME, "w", newline="") as file:

            fieldnames = [
                "Case ID",
                "Crime Type",
                "Location",
                "Date",
                "Officer",
                "Status"
            ]

            writer = csv.DictWriter(
                file,
                fieldnames=fieldnames
            )

            writer.writeheader()
            writer.writerows(records)

        print("\nCrime Record Updated Successfully!")

    else:

        print("\nCase ID Not Found.")


# ============================================================
# DELETE CRIME
# ============================================================

def delete_crime():

    create_file()

    case_id = input("\nEnter Case ID to Delete : ")

    records = []
    found = False

    with open(FILE_NAME, "r") as file:

        reader = csv.DictReader(file)

        for row in reader:

            if row["Case ID"] == case_id:

                found = True
                continue

            records.append(row)

    if found:

        with open(FILE_NAME, "w", newline="") as file:

            fieldnames = [
                "Case ID",
                "Crime Type",
                "Location",
                "Date",
                "Officer",
                "Status"
            ]

            writer = csv.DictWriter(
                file,
                fieldnames=fieldnames
            )

            writer.writeheader()
            writer.writerows(records)

        print("\nCrime Record Deleted Successfully!")

    else:

        print("\nCase ID Not Found.")


# ============================================================
# CRIME MENU
# ============================================================

def crime_menu():

    create_file()

    while True:

        print("\n")
        print("=" * 50)
        print("           CRIME MANAGEMENT SYSTEM")
        print("=" * 50)

        print("1. Add Crime")
        print("2. View Crimes")
        print("3. Search Crime")
        print("4. Update Crime")
        print("5. Delete Crime")
        print("6. Exit")

        print("=" * 50)

        choice = input("Enter Choice : ")

        if choice == "1":

            add_crime()

        elif choice == "2":

            view_crimes()

        elif choice == "3":

            search_crime()

        elif choice == "4":

            update_crime()

        elif choice == "5":

            delete_crime()

        elif choice == "6":

            print("\nThank you for using Crime Management System!")
            break

        else:

            print("\nInvalid Choice! Please try again.")


# ============================================================
# MAIN PROGRAM
# ============================================================

if __name__ == "__main__":

    crime_menu()