def add_contact(contacts):
    name = input("Enter Name: ")
    if not name.isalpha():
        print("Error: Name must be a string.")
        return
    phone = input("Enter Phone Number: ")
    if not phone.isdigit():
        print("Error: Phone number must be numeric.")
        return
    if phone in [contact['Phone'] for contact in contacts]:
        print("Error: Phone number already exists.")
        return
    email = input("Enter Email: ")
    address = input("Enter Address: ")
    contact = {"Name": name, "Phone": phone, "Email": email, "Address": address}
    contacts.append(contact)
    print("Contact added successfully.")

def view_contacts(contacts):
    if not contacts:
        print("No contacts found.")
        return
    print("Contacts List:")
    for idx, contact in enumerate(contacts, start=1):
        print(f"{idx}. {contact['Name']} | {contact['Phone']} | {contact['Email']} | {contact['Address']}")
def remove_contact(contacts):
    phone = input("Enter Phone Number of Contact to Remove: ")
    for contact in contacts:
        if contact['Phone'] == phone:
            contacts.remove(contact)
            print("Contact removed successfully.")
            return
    print("Error: Contact not found.")

def search_contacts(contacts):
    query = input("Enter Name or Phone to Search: ")
    results = [c for c in contacts if query in c['Name'] or query in c['Phone']]
    if results:
        print("Search Results:")
        for contact in results:
            print(f"{contact['Name']} | {contact['Phone']} | {contact['Email']} | {contact['Address']}")
    else:
        print("No contacts found.")
