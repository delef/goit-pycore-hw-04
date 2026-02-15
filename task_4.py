def parse_input(user_input):
    parts = user_input.split()
    if not parts:
        return "", []
    cmd = parts[0].strip().lower()
    return cmd, parts[1:]

def add_contact(args, contacts):
    if len(args) != 2:
        return "Please enter both name and phone."
    name, phone = args
    contacts[name] = phone
    return "Contact added."

def change_contact(args, contacts):
    if len(args) != 2:
        return "Please enter both name and new phone."
    name, phone = args
    if name not in contacts:
        return "Contact not found."
    contacts[name] = phone
    return "Contact updated."

def show_phone(args, contacts):
    if len(args) != 1:
        return "Please enter the name."
    name = args[0]
    return contacts.get(name, "Contact not found.")

def show_all(contacts):
    if not contacts:
        return "No contacts found."
    return "\n".join(f"{name}: {phone}" for name, phone in contacts.items())

def main():
    contacts = {}
    print("Welcome to the assistant bot!")

    handlers = {
        "add": lambda args: add_contact(args, contacts),
        "change": lambda args: change_contact(args, contacts),
        "phone": lambda args: show_phone(args, contacts),
        "all": lambda args: show_all(contacts),
    }

    while True:
        user_input = input("Enter a command: ")
        command, args = parse_input(user_input)

        if command in ("close", "exit"):
            print("Good bye!")
            break
        elif command == "hello":
            print("How can I help you?")
        elif command in handlers:
            print(handlers[command](args))
        else:
            print("Invalid command.")

if __name__ == "__main__":
    main()
