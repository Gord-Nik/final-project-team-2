contacts = {}


def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args


def add_contact(args):
    name, phone = args
    contacts[name] = phone
    return "Contact added."


def change_contact(args):
    name, new_phone = args
    if name in contacts:
        contacts[name] = new_phone
        return "Contact updated."
    else:
        return "Contact not found."


def show_phone(args):
    name = args[0]
    if name in contacts:
        return contacts[name]
    else:
        return "Contact not found."


def main():
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        command, *args = parse_input(user_input)

        if command in ["close", "exit"]:
            print("Good bye!")
            break
        elif command == "hello":
            print("How can I help you?")
        elif command == "add":
            print(add_contact(args))
        elif command == "change":
            print(change_contact(args))
        elif command == "phone":
            print(show_phone(args))
        elif command == "all":
            print(contacts)
        else:
            print("Invalid command.")


if __name__ == "__main__":
    main()
