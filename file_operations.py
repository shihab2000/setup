def save_to_file(contacts, filename="contacts.txt"):
    with open(filename, "w") as file:
        for contact in contacts:
            file.write(f"{contact['Name']},{contact['Phone']},{contact['Email']},{contact['Address']}\n")


