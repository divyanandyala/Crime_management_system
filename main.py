from authentication import login
from crime_menu import crime_menu
from fir_menu import fir_menu
from evidence import evidence_menu
from crime_analyise import crime_analysis


def main():

    print("=" * 50)
    print("CRIME MANAGEMENT SYSTEM")
    print("=" * 50)

    # Login Authentication
    if not login():
        print("Access Denied!")
        return

    while True:

        print("\n========== MAIN MENU ==========")
        print("1. Crime Management")
        print("2. FIR Management")
        print("3. Evidence Management")
        print("4. Crime Analysis")
        print("5. Exit")
        print("=" * 30)

        choice = input("Enter your choice: ")

        if choice == "1":
            crime_menu()

        elif choice == "2":
            fir_menu()

        elif choice == "3":
            evidence_menu()

        elif choice == "4":
            crime_analysis()

        elif choice == "5":
            print("\nThank You for Using Crime Management System")
            print("Exiting...")
            break

        else:
            print("Invalid Choice! Please Try Again.")


if __name__ == "__main__":
    main()