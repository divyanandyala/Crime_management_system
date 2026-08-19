import csv
import os

USER_FILE = "users.csv"


# Create default admin user
def create_default_user():

    if not os.path.exists(USER_FILE):

        with open(USER_FILE, "w", newline="") as file:

            writer = csv.writer(file)

            writer.writerow(["Username", "Password"])
            writer.writerow(["admin", "admin123"])


# Login Function
def login():

    create_default_user()

    print("\n========== LOGIN ==========")

    username = input("Enter Username : ")
    password = input("Enter Password : ")

    with open(USER_FILE, "r") as file:

        reader = csv.DictReader(file)

        for row in reader:

            if row["Username"] == username and row["Password"] == password:

                print("\nLogin Successful!")
                return True

    print("\nInvalid Username or Password!")
    return False


# Change Password
def change_password():

    username = input("Enter Username : ")
    old_password = input("Enter Old Password : ")
    new_password = input("Enter New Password : ")

    records = []
    found = False

    with open(USER_FILE, "r") as file:

        reader = csv.DictReader(file)

        for row in reader:

            if row["Username"] == username and row["Password"] == old_password:

                row["Password"] = new_password
                found = True

            records.append(row)

    if found:

        with open(USER_FILE, "w", newline="") as file:

            fieldnames = ["Username", "Password"]

            writer = csv.DictWriter(file, fieldnames=fieldnames)

            writer.writeheader()
            writer.writerows(records)

        print("Password Changed Successfully!")

    else:

        print("Invalid Username or Password!")


# Authentication Menu
def authentication_menu():

    while True:

        print("\n========== AUTHENTICATION ==========")
        print("1. Login")
        print("2. Change Password")
        print("3. Exit")

        choice = input("Enter Choice : ")

        if choice == "1":

            if login():
                return True

        elif choice == "2":

            change_password()

        elif choice == "3":

            return False

        else:

            print("Invalid Choice!")


if __name__ == "__main__":
    authentication_menu()