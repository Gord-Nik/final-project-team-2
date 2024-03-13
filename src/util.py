from docutils import DataError
from src.models import AddressBook, Record

def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError:
            return "Give me name,phone, address and e-mail  please."
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
    def add_contact(self, args):
        name, phone, address, email, birthday = args
        name = ''.join(name)
        phone = ''.join(phone)
        address = ''.join(address)
        email = ''.join(email)
        birthday = ''.join(birthday)
        record = Record(name)
        record.add_phone(phone)
        record.add_birthday(birthday)
        # Додайте методи для email та address, якщо потрібно
        return self.addressBook.add_record(record)


    @input_error
    def remove_contact(self, args):
        name = ''.join(args)
        return self.addressBook.remove_contact(name)

    @input_error
    def get_phone(self, args):
        name = ''.join(args)
        return self.addressBook.get_phone(name)

    @input_error
    def change_phone(self, args):
        name, phone, new_phone = args
        name = ''.join(name)
        phone = ''.join(phone)
        new_phone = ''.join(new_phone)
        return self.addressBook.change_phone(name, phone, new_phone)

    @input_error
    def remove_phone(self, args):
        name, phone = args
        name = ''.join(name)
        phone = ''.join(phone)
        return self.addressBook.remove_phone(name, phone)
    
    @input_error
    def add_email(self, args):
        name, email = args
        name = ''.join(name)
        email = ''.join(email)
        return self.addressBook.add_email(name, email)

    @input_error
    def edit_email(self, args):
        name, old_email, new_email = args
        name = ''.join(name)
        old_email = ''.join(old_email)
        new_email = ''.join(new_email)
        return self.addressBook.edit_email(name, old_email, new_email)

    @input_error
    def remove_email(self, args):
        name, email = args
        name = ''.join(name)
        email = ''.join(email)
        return self.addressBook.remove_email(name, email)

    @input_error
    def add_address(self, args):
        name, address = args
        name = ''.join(name)
        address = ''.join(address)
        return self.addressBook.add_address(name, address)

    @input_error
    def edit_address(self, args):
        name, old_address, new_address = args
        name = ''.join(name)
        old_address = ''.join(old_address)
        new_address = ''.join(new_address)
        return self.addressBook.edit_address(name, old_address, new_address)

    @input_error
    def remove_address(self, args):
        name, address = args
        name = ''.join(name)
        address = ''.join(address)
        return self.addressBook.remove_address(name, address)

    @input_error
    def add_birthday(self, args):
        name, birthday = args
        name = ''.join(name)
        birthday = ''.join(birthday)
        return self.addressBook.add_birthday(name, birthday)

    @input_error
    def show_birthday(self, args):
        name = ''.join(args)
        return self.addressBook.show_birthday(name)

    def all(self):
        return self.addressBook.show_all_contacts()

    def birthdays(self):
        return self.addressBook.get_birthdays_per_week()

    def exit(self):
        self.addressBook.exit()