from src.util import Bot_Util
from src.models import AddressBook


def main():
    pass
    helper = Bot_Util(AddressBook())
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        command, *args = helper.parse_input(user_input)

        if command.strip() in ["close", "exit"]:
            helper.exit()
            print("Good bye!")
            break
        elif command == "hello":
            print("How can I help you?")
        elif command == "add":
            print(helper.add_contact(args))
        elif command == "remove":
            print(helper.remove_contact(args))
        elif command == "change":
            print(helper.change_phone(args))
        elif command == "phone":
            print(helper.get_phone(args))
        elif command == "remove-phone":
            print(helper.remove_phone(args))
        elif command == "add-birthday":
            print(helper.add_birthday(args))
        elif command == "show-birthday":
            print(helper.show_birthday(args))
        elif command == "add-email":
            print(helper.add_email(args))
        elif command == "edit-email":
            print(helper.edit_email(args))
        elif command == "remove-email":
            print(helper.remove_email(args))
        elif command == "add-address":
            print(helper.add_address(args))
        elif command == "edit-address":
            print(helper.edit_address(args))
        elif command == "remove-address":
            print(helper.remove_address(args))
        elif command == "all":
            print(helper.all())
        elif command == "birthdays":
            print(helper.birthdays())
        elif command == "close":
            helper.exit()
        else:
            print("Invalid command.")
#
#
# if __name__ == "__main__":
#     main()
