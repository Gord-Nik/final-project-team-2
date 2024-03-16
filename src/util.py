from docutils import DataError
from src.models import AddressBook, Record


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


class BotUtil:
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

    # CUD e-mail
    @input_error
    def add_email(self, args):
        name, email = args
        name = ''.join(name)
        email = ''.join(email)
        return self.addressBook.add_email(name, email)

    @input_error
    def change_email(self, args):
        name, email = args
        name = ''.join(name)
        email = ''.join(email)
        return self.addressBook.edit_email(name, email)

    @input_error
    def show_email(self, args):
        name = args
        name = ''.join(name)
        return self.addressBook.show_email(name)

    @input_error
    def add_address(self, args):
        name, address = args
        name = ''.join(name)
        address = ''.join(address)
        return self.addressBook.add_address(name, address)

    @input_error
    def change_address(self, args):
        name, address = args
        name = ''.join(name)
        address = ''.join(address)
        return self.addressBook.edit_address(name, address)

    @input_error
    def show_address(self, args):
        name = args
        name = ''.join(name)
        return self.addressBook.show_address(name)

    @input_error
    def add_birthday(self, args):
        name, birthday = args
        name = ''.join(name)
        birthday = ''.join(birthday)
        return self.addressBook.add_birthday(name, birthday)

    @input_error
    def change_birthday(self, args):
        name, birthday = args
        name = ''.join(name)
        birthday = ''.join(birthday)
        return self.addressBook.edit_birthday(name, birthday)

    @input_error
    def show_birthday(self, args):
        name = args
        name = ''.join(name)
        return self.addressBook.show_birthday(name)

    def birthdays(self, args):
        count_of_days = int(args[0])
        return self.addressBook.get_birthdays_by_count_of_days(count_of_days)

    def all(self):
        return self.addressBook

    def exit(self):
        self.addressBook.exit()
