def load_from_file(filename="contacts.txt"):
    contacts = []
    try:
        with open(filename, "r") as file:
            for line in file:
                name, phone, email, address = line.strip().split(",")
                contacts.append({"Name": name, "Phone": phone, "Email": email, "Address": address})
    except FileNotFoundError:
        print("No saved contacts found. Starting fresh.")
    return contacts