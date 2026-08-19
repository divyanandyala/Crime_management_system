import csv
import os

FILE_NAME = "fir_records.csv"


# Create CSV File
def create_file():

    if not os.path.exists(FILE_NAME):

        with open(FILE_NAME, "w", newline="") as file:

            writer = csv.writer(file)

            writer.writerow([
                "FIR ID",
                "Complainant",
                "Crime Type",
                "Location",
                "Date",
                "Status"
            ])


# Add FIR
def add_fir():

    create_file()

    fir_id = input("Enter FIR ID : ")
    complainant = input("Enter Complainant Name : ")
    crime_type = input("Enter Crime Type : ")
    location = input("Enter Location : ")
    date = input("Enter Date (DD-MM-YYYY) : ")
    status = input("Enter Status (Open/Closed) : ")

    with open(FILE_NAME, "a", newline="") as file:

        writer = csv.writer(file)

        writer.writerow([
            fir_id,
            complainant,
            crime_type,
            location,
            date,
            status
        ])

    print("FIR Record Added Successfully!")


# View FIR Records
def view_firs():

    create_file()

    with open(FILE_NAME, "r") as file:

        reader = csv.reader(file)

        print("\n========== FIR RECORDS ==========")

        for row in reader:
            print(row)


# Search FIR
def search_fir():

    fir_id = input("Enter FIR ID : ")

    with open(FILE_NAME, "r") as file:

        reader = csv.DictReader(file)

        found = False

        for row in reader:

            if row["FIR ID"] == fir_id:

                print("\nFIR Record Found")
                print(row)
                found = True
                break

        if not found:
            print("FIR Record Not Found.")


# Update FIR
def update_fir():

    fir_id = input("Enter FIR ID : ")

    records = []

    with open(FILE_NAME, "r") as file:

        reader = csv.DictReader(file)

        found = False

        for row in reader:

            if row["FIR ID"] == fir_id:

                row["Complainant"] = input("New Complainant : ")
                row["Crime Type"] = input("New Crime Type : ")
                row["Location"] = input("New Location : ")
                row["Date"] = input("New Date : ")
                row["Status"] = input("New Status : ")

                found = True

            records.append(row)

    if found:

        with open(FILE_NAME, "w", newline="") as file:

            fieldnames = [
                "FIR ID",
                "Complainant",
                "Crime Type",
                "Location",
                "Date",
                "Status"
            ]

            writer = csv.DictWriter(file, fieldnames=fieldnames)

            writer.writeheader()
            writer.writerows(records)

        print("FIR Record Updated Successfully!")

    else:

        print("FIR ID Not Found.")


# Delete FIR
def delete_fir():

    fir_id = input("Enter FIR ID : ")

    records = []

    found = False

    with open(FILE_NAME, "r") as file:

        reader = csv.DictReader(file)

        for row in reader:

            if row["FIR ID"] == fir_id:
                found = True
                continue

            records.append(row)

    if found:

        with open(FILE_NAME, "w", newline="") as file:

            fieldnames = [
                "FIR ID",
                "Complainant",
                "Crime Type",
                "Location",
                "Date",
                "Status"
            ]

            writer = csv.DictWriter(file, fieldnames=fieldnames)

            writer.writeheader()
            writer.writerows(records)

        print("FIR Record Deleted Successfully!")

    else:

        print("FIR ID Not Found.")


# FIR Menu
def fir_menu():

    while True:

        print("\n========== FIR MENU ==========")
        print("1. Add FIR")
        print("2. View FIR Records")
        print("3. Search FIR")
        print("4. Delete FIR")
        print("5. Back to Main Menu")

        choice = input("Enter Choice : ")

        if choice == "1":
            add_fir()

        elif choice == "2":
            view_firs()

        elif choice == "3":
            search_fir()

        elif choice == "4":
            delete_fir()

        elif choice == "5":
            break

        else:
            print("Invalid Choice!")


if __name__ == "__main__":
    fir_menu()