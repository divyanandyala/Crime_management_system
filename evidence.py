import csv
import os

FILE_NAME = "evidence_records.csv"


# Create CSV File
def create_file():

    if not os.path.exists(FILE_NAME):

        with open(FILE_NAME, "w", newline="") as file:

            writer = csv.writer(file)

            writer.writerow([
                "Evidence ID",
                "Case ID",
                "Evidence Type",
                "Description",
                "Collected By",
                "Date"
            ])


# Add Evidence
def add_evidence():

    create_file()

    evidence_id = input("Enter Evidence ID : ")
    case_id = input("Enter Case ID : ")
    evidence_type = input("Enter Evidence Type : ")
    description = input("Enter Description : ")
    collected_by = input("Collected By : ")
    date = input("Enter Date (DD-MM-YYYY) : ")

    with open(FILE_NAME, "a", newline="") as file:

        writer = csv.writer(file)

        writer.writerow([
            evidence_id,
            case_id,
            evidence_type,
            description,
            collected_by,
            date
        ])

    print("Evidence Record Added Successfully!")


# View Evidence
def view_evidence():

    create_file()

    with open(FILE_NAME, "r") as file:

        reader = csv.reader(file)

        print("\n========== EVIDENCE RECORDS ==========")

        for row in reader:
            print(row)


# Search Evidence
def search_evidence():

    evidence_id = input("Enter Evidence ID : ")

    with open(FILE_NAME, "r") as file:

        reader = csv.DictReader(file)

        found = False

        for row in reader:

            if row["Evidence ID"] == evidence_id:

                print("\nEvidence Record Found")
                print(row)
                found = True
                break

        if not found:
            print("Evidence Record Not Found.")


# Update Evidence
def update_evidence():

    evidence_id = input("Enter Evidence ID : ")

    records = []

    with open(FILE_NAME, "r") as file:

        reader = csv.DictReader(file)

        found = False

        for row in reader:

            if row["Evidence ID"] == evidence_id:

                row["Case ID"] = input("New Case ID : ")
                row["Evidence Type"] = input("New Evidence Type : ")
                row["Description"] = input("New Description : ")
                row["Collected By"] = input("Collected By : ")
                row["Date"] = input("New Date : ")

                found = True

            records.append(row)

    if found:

        with open(FILE_NAME, "w", newline="") as file:

            fieldnames = [
                "Evidence ID",
                "Case ID",
                "Evidence Type",
                "Description",
                "Collected By",
                "Date"
            ]

            writer = csv.DictWriter(file, fieldnames=fieldnames)

            writer.writeheader()
            writer.writerows(records)

        print("Evidence Record Updated Successfully!")

    else:
        print("Evidence ID Not Found.")


# Delete Evidence
def delete_evidence():

    evidence_id = input("Enter Evidence ID : ")

    records = []

    found = False

    with open(FILE_NAME, "r") as file:

        reader = csv.DictReader(file)

        for row in reader:

            if row["Evidence ID"] == evidence_id:
                found = True
                continue

            records.append(row)

    if found:

        with open(FILE_NAME, "w", newline="") as file:

            fieldnames = [
                "Evidence ID",
                "Case ID",
                "Evidence Type",
                "Description",
                "Collected By",
                "Date"
            ]

            writer = csv.DictWriter(file, fieldnames=fieldnames)

            writer.writeheader()
            writer.writerows(records)

        print("Evidence Record Deleted Successfully!")

    else:
        print("Evidence ID Not Found.")


# Evidence Menu
def evidence_menu():

    while True:

        print("\n========== EVIDENCE MENU ==========")
        print("1. Add Evidence")
        print("2. View Evidence")
        print("3. Search Evidence")
        print("4. Update Evidence")
        print("5. Delete Evidence")
        print("6. Back to Main Menu")

        choice = input("Enter Choice : ")

        if choice == "1":
            add_evidence()

        elif choice == "2":
            view_evidence()

        elif choice == "3":
            search_evidence()

        elif choice == "4":
            update_evidence()

        elif choice == "5":
            delete_evidence()

        elif choice == "6":
            break

        else:
            print("Invalid Choice!")


if __name__ == "__main__":
    evidence_menu()