import json

def load_contacts():
    try:
        with open("Contacts.txt", "r") as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        return {}

def save_contacts():
    with open("Contacts.txt", "w") as f:
        json.dump(contacts, f, indent=4)

def display_contacts():
    if not contacts:
        print("Empty contact list.")
    else:
        print("Name\t\tContact Number\t\tEmail Address")
        for name, info in contacts.items():
            if isinstance(info, dict):
                phone = info.get("phone", "N/A")
                email = info.get("email", "N/A")
            else:
                # Handle legacy data where info might be a phone number string
                phone = info
                email = "N/A"
            print(f"{name}\t\t{phone}\t\t{email}")

contacts = load_contacts()

while True:
    print("\n1. Add contact")
    print("2. Display contacts")
    print("3. Edit contact")
    print("4. Delete contact")
    print("5. Exit")

    choice = input("Enter your choice: ")
    if choice == '1':
        name = input("Enter contact name: ")
        phone = input("Enter phone number: ")
        email = input("Enter email address: ")
        contacts[name] = {"phone": phone, "email": email}
        print(f"Contact {name} added successfully.")
        save_contacts()
        
    elif choice == '2':
        display_contacts()
        
    elif choice == '3':
        name_to_edit = input("Enter contact name to edit: ")
        if name_to_edit in contacts:
            new_phone = input("Enter new phone number (leave blank to keep current): ")
            new_email = input("Enter new email address (leave blank to keep current): ")
            if new_phone:
                contacts[name_to_edit]["phone"] = new_phone
            if new_email:
                contacts[name_to_edit]["email"] = new_email
            print(f"Contact {name_to_edit} updated successfully.")
            save_contacts()
        else:
            print("Contact not found.")
            
    elif choice == '4':
        name_to_delete = input("Enter contact name to delete: ")
        if name_to_delete in contacts:
            confirm = input("Are you sure you want to delete this contact? (y/n): ").lower()
            if confirm == 'y':
                del contacts[name_to_delete]
                print(f"Contact {name_to_delete} deleted successfully.")
                save_contacts()
            else:
                print("Deletion cancelled.")
        else:
            print("Contact not found.")
            
    elif choice == '5':
        break

    else:
        print("Invalid choice. Please try again.")
