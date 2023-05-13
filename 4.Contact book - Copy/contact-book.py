contacts = {}
def add_contact():
    name = input("Enter the contact name: ")
    phone = input("Enter the contact phone number: ")
    email = input("Enter the contact email address: ")
    contacts[name] = {"phone": phone, "email": email}
    print(f"Contact {name} added successfully!")
def search_contact():
    name = input("Enter the contact name: ")
    if name in contacts:
        print(f"Name: {name}")
        print(f"Phone: {contacts[name]['phone']}")
        print(f"Email: {contacts[name]['email']}")
    else:
        print(f"Contact {name} not found.")
def display_contacts():
    for name, contact in contacts.items():
        print(f"Name: {name}")
        print(f"Phone: {contact['phone']}")
        print(f"Email: {contact['email']}")
        print()
def delete_contact():
    name = input("Enter the contact name to delete: ")
    if name in contacts:
        del contacts[name]
        print(f"Contact {name} deleted successfully!")
    else:
        print(f"Contact {name} not found.")
def show_menu():
    print("1. Add Contact")
    print("2. Search Contact")
    print("3. Display All Contacts")
    print("4. Delete Contact")
    print("5. Quit")
    choice = input("Enter your choice: ")
    return choice
while True:
    choice = show_menu()
    if choice == "1":
        add_contact()
    elif choice == "2":
        search_contact()
    elif choice == "3":
        display_contacts()
    elif choice == "4":
        delete_contact()
    elif choice == "5":
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.")
