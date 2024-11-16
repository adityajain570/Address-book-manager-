import json

class AddressBook:
    def __init__(self, filename="address_book.json"):
        self.filename = filename
        self.contacts = self.load_contacts()

    def load_contacts(self):
        """ Load contacts from a JSON file """
        try:
            with open(self.filename, 'r') as file:
                return json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            return {}

    def save_contacts(self):
        """ Save contacts to a JSON file """
        with open(self.filename, 'w') as file:
            json.dump(self.contacts, file, indent=4)

    def add_contact(self, name, phone, email, address):
        """ Add a new contact """
        if name in self.contacts:
            print(f"Contact with name {name} already exists.")
        else:
            self.contacts[name] = {
                "phone": phone,
                "email": email,
                "address": address
            }
            self.save_contacts()
            print(f"Contact {name} added successfully.")

    def search_contact(self, name):
        """ Search for a contact by name """
        contact = self.contacts.get(name)
        if contact:
            print(f"Details for {name}:")
            print(f"Phone: {contact['phone']}")
            print(f"Email: {contact['email']}")
            print(f"Address: {contact['address']}")
        else:
            print(f"Contact with name {name} not found.")

    def list_contacts(self):
        """ List all contacts """
        if not self.contacts:
            print("No contacts found.")
        else:
            for name, details in self.contacts.items():
                print(f"Name: {name}")
                print(f"  Phone: {details['phone']}")
                print(f"  Email: {details['email']}")
                print(f"  Address: {details['address']}")
                print("-" * 20)

    def update_contact(self, name, phone=None, email=None, address=None):
        """ Update an existing contact """
        contact = self.contacts.get(name)
        if contact:
            if phone:
                contact["phone"] = phone
            if email:
                contact["email"] = email
            if address:
                contact["address"] = address
            self.save_contacts()
            print(f"Contact {name} updated successfully.")
        else:
            print(f"Contact with name {name} not found.")

    def delete_contact(self, name):
        """ Delete a contact """
        if name in self.contacts:
            del self.contacts[name]
            self.save_contacts()
            print(f"Contact {name} deleted successfully.")
        else:
            print(f"Contact with name {name} not found.")

# Menu interface
def display_menu():
    print("\n=== Address Book Menu ===")
    print("1. Add Contact")
    print("2. Search Contact")
    print("3. List All Contacts")
    print("4. Update Contact")
    print("5. Delete Contact")
    print("6. Exit")

def main():
    address_book = AddressBook()

    while True:
        display_menu()
        choice = input("Choose an option: ").strip()

        if choice == '1':
            name = input("Enter name: ").strip()
            phone = input("Enter phone number: ").strip()
            email = input("Enter email: ").strip()
            address = input("Enter address: ").strip()
            address_book.add_contact(name, phone, email, address)

        elif choice == '2':
            name = input("Enter name to search: ").strip()
            address_book.search_contact(name)

        elif choice == '3':
            address_book.list_contacts()

        elif choice == '4':
            name = input("Enter name to update: ").strip()
            phone = input("Enter new phone number (leave blank to keep current): ").strip() or None
            email = input("Enter new email (leave blank to keep current): ").strip() or None
            address = input("Enter new address (leave blank to keep current): ").strip() or None
            address_book.update_contact(name, phone, email, address)

        elif choice == '5':
            name = input("Enter name to delete: ").strip()
            address_book.delete_contact(name)

        elif choice == '6':
            print("Exiting Address Book Manager.")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()

