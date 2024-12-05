from contacts import add_contact
from file_operations import save_to_file
from contacts import view_contacts
from contacts import remove_contact
from contacts import search_contacts
from validators import load_from_file
def main():
    contacts = load_from_file()
    while True:
        print("\nContact Book Menu")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Remove Contact")
        print("4. Search Contacts")
        print("5. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            add_contact(contacts)
            save_to_file(contacts)
        elif choice == "2":
            view_contacts(contacts)
        elif choice == "3":
            remove_contact(contacts)
            save_to_file(contacts)
        elif choice == "4":
            search_contacts(contacts)
        elif choice == "5":
            print("Exiting... Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
