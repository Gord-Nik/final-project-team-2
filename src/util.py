from docutils import DataError
from src.models import AddressBook, Record, Notes


def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError:
            return "Give me name and phone please."
        except KeyError:
            return "Enter correct arguments please."
        except IndexError:
            return "Give me name and phone please."
        except DataError as e:
            return f"{e}"
        except Exception as e:
            return f"An unexpected error occurred: {e}"

    return inner


class Bot_Util:
    def __init__(self, addressBook: AddressBook):
        self.addressBook = addressBook

    def parse_input(self, user_input):
        cmd, *args = user_input.split()
        cmd = cmd.strip().lower()
        return cmd, *args

    @input_error
    def add_contact_or_phone(self, args):
        name, phone = args
        name = ''.join(name)
        phone = ''.join(phone)
        if self.addressBook.if_contact_exists(name):
            return self.addressBook.add_phone(name, phone)
        record = Record(name)
        record.add_phone(phone)
        return self.addressBook.add_record(record)

    @input_error
    def remove_contact(self, args):
        name = args
        name = ''.join(name)
        return self.addressBook.remove(name)

    @input_error
    def get_phone(self, args):
        name = args
        name = ''.join(name)
        return self.addressBook.find(name)

    @input_error
    def change_phone(self, args):
        name, phone, new_phone = args
        name = ''.join(name)
        phone = ''.join(phone)
        new_phone = ''.join(new_phone)
        return self.addressBook.edit_phone(name, phone, new_phone)

    @input_error
    def remove_phone(self, args):
        name, phone = args
        name = ''.join(name)
        phone = ''.join(phone)
        return self.addressBook.remove_phone(name, phone)

    @input_error
    def add_birthday(self, args):
        name, birthday = args
        name = ''.join(name)
        birthday = ''.join(birthday)
        return self.addressBook.add_birthday(name, birthday)

    @input_error
    def show_birthday(self, args):
        name = args
        name = ''.join(name)
        return self.addressBook.show_birthday(name)

    def all(self):
        return self.addressBook

    def birthdays(self):
        return self.addressBook.get_birthdays_per_week()
    
    def exit(self):
        self.addressBook.exit()
    
    def make_note():
        named_note = input("What's the note's name? >>>")
        print(f"{named_note} created! You can type now (type 'close' when finished):\n")
        lines = []
        while True:
            line = input()
            if line in ['close', 'exit', 'finish', 'done', 'save']:
                break
            lines.append(line)
            new_note = {named_note: '\n'.join(lines)}
        return new_note

    


