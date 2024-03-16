from prompt_toolkit import PromptSession
from prompt_toolkit.completion import WordCompleter
from src.util import BotUtil
from src.models import AddressBook
import src.notes_bot


def main():
    command_list = ['hello',
                    'add',
                    'remove',
                    'change',
                    'phone',
                    'remove-phone',
                    "add-birthday",
                    "show-birthday",
                    "all",
                    "birthdays",
                    "open-notes",
                    'close',
                    'exit',
                    'change-birthday'
                    ]
    session = PromptSession()
    completer = WordCompleter(command_list)
    helper = BotUtil(AddressBook())
    print("Welcome to the assistant bot!")
    while True:
        user_input = session.prompt("Enter a command: ", completer=completer)
        command, *args = helper.parse_input(user_input)

        if command.strip() in ["close", "exit"]:
            print("Good bye!")
            helper.exit()
            break
        elif command == "hello":
            print("How can I help you?")
        elif command == "add":
            print(helper.add_contact_or_phone(args))
        elif command == "add-address":
            print(helper.add_address(args))
        elif command == "show-address":
            print(helper.show_address(args))
        elif command == "change-address":
            print(helper.change_address(args))
        elif command == "add-email":
            print(helper.add_email(args))
        elif command == "show-email":
            print(helper.show_email(args))
        elif command == "change-email":
            print(helper.change_email(args))
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
        elif command == "change-birthday":
            print(helper.change_birthday(args))
        elif command == "birthdays":
            print(helper.birthdays(args))
        elif command == "all":
            print(helper.all())
        elif command == "open-notes":
            src.notes_bot.open_notes()
        elif command == "close":
            print("Good bye!")
            helper.exit()
        else:
            print("Invalid command.")
