from prompt_toolkit import PromptSession
from prompt_toolkit.completion import WordCompleter
from src.util import Bot_Util
from src.models import AddressBook
import src.notes_bot



def main():
    command_list = ['hello', 'add', 'remove', 'change', 'phone', 'remove-phone', "add-birthday", "show-birthday", "all", "birthdays", "open-notes", 'close', 'exit']
    session = PromptSession()
    completer = WordCompleter(command_list)
    helper = Bot_Util(AddressBook())
    print("Welcome to the assistant bot!")
    while True:
        user_input = session.prompt("Enter a command: ", completer=completer)
        command, *args = helper.parse_input(user_input)

        if command.strip() in ["close", "exit"]:
            helper.exit()
            print("Good bye!")
            break
        elif command == "hello":
            print("How can I help you?")
        elif command == "add":
            print(helper.add_contact_or_phone(args))
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
        elif command == "all":
            print(helper.all())
        elif command == "birthdays":
            print(helper.birthdays())
        elif command == "open-notes":
            src.notes_bot.open_notes()
        elif command == "close":
            helper.exit()
        else:
            print("Invalid command.")


if __name__ == "__main__":
    main()
