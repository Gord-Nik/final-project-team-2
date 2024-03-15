import datetime
import re
import os
import sys
import pickle
from collections import UserDict, defaultdict
from docutils import DataError


class Field:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)

class Name(Field):
    def __init__(self, name):
        super().__init__(name)

    def __hash__(self):
        return hash(self.value)

    def __eq__(self, other):
        return self.value == other.value

class Phone(Field):
    __pattern = r'^\d{10}$'

    def __init__(self, phone):
        if not re.match(self.__pattern, phone):
            raise ValueError("Phone should contains 10 digits only")
        super().__init__(phone)

    def __hash__(self):
        return hash(self.value)

    def __eq__(self, other):
        return self.value == other.value

class Email(Field):
    __pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'

    def __init__(self, email):
        if not re.match(self.__pattern, email):
            raise ValueError("Invalid email format")
        super().__init__(email)

class Address(Field):
    def __init__(self, address):
        super().__init__(address)

class Birthday(Field):
    __date_format = "%d.%m.%Y"
    def __init__(self, birthday):
        try:
            value = datetime.datetime.strptime(birthday, self.__date_format)
        except ValueError:
            raise DataError("Incorrect date, should be format 'dd.mm.YYYY'")
        super().__init__(value)

    def __str__(self):
        return f"{self.value.strftime(self.__date_format)}"

class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []
        self.email = None
        self.address = None
        self.birthday = None

    def add_phone(self, phone):
        phn = Phone(phone)
        self.phones.append(phn)
        return "Phone was added."
    
    def edit_phone(self, phone, new_phone):
        phn = Phone(phone)
        if self.__phone_exists(phn):
            self.phones.remove(phn)
            self.phones.append(Phone(new_phone))
            return "Phone was edited."
        raise KeyError

    def find_phone(self, phone):
        phn = Phone(phone)
        if self.__phone_exists(phn):
            return phn
        raise KeyError

    def remove_phone(self, phone):
        phn = Phone(phone)
        if self.__phone_exists(phn):
            self.phones.remove(phn)
            return "Phone was removed."
        raise KeyError

    def add_email(self, email):
        if self.email:
            raise ValueError
        self.email = Email(email)
        return "E-mail was added."

    def edit_email(self, email):
        self.email = Email(email)
        return "Email was edited."

    def show_email(self):
        return self.email

    def add_address(self, address):
        if self.address:
            raise ValueError
        self.address = Address(address)
        return "Address was added."

    def edit_address(self, address):
        self.address = Address(address)
        return "Address was edited."
    
    def show_address(self):
        return self.address
    
    def add_birthday(self, birthday):
        if self.birthday:
            raise ValueError
        self.birthday = Birthday(birthday)
        return "Birthday was added."

    def edit_birthday(self, birthday):
        self.birthday = Birthday(birthday)
        return "Birthday was edited."

    def show_birthday(self):
        return self.birthday
    
    def __phone_exists(self, phone):
        return phone in self.phones
    
    def __str__(self):
        brth = ""
        if self.birthday is not None:
            brth += f" birthday: {self.birthday},"
        
        mail = ""
        if self.email is not None:
            mail += f" e-mail: {self.email},"
        
        addr = ""
        if self.address is not None:
            addr += f" address: {self.address}."

        return (f"Contact name: {self.name.value},"
                f" phones: {'; '.join(p.value for p in self.phones)},{brth}{mail}{addr}")

class AddressBook(UserDict):
    __file_name = "data.bin"
    __path = os.path.join(os.getcwd(), __file_name)

    def __init__(self):
        UserDict.__init__(self)
        if os.path.isfile(self.__path):
            self.data = self.__read_from_file()
    
    def __save_to_file(self):
        with open(self.__path, "wb") as file:
            pickle.dump(self.data, file)

    def __read_from_file(self):
        with open(self.__path, "rb") as file:
            return pickle.load(file)
    
    def add_record(self, data):
        if data in self.data.values():
            raise ValueError
        self.data[data.name] = data
        return "Contact was added."

    def find(self, name):
        nm = Name(name)
        if self.__has_key(nm):
            return self.data[nm]
        return None

    def if_contact_exists(self, name):
        return self.__has_key(Name(name))

    def add_phone(self, name, phone):
        nm = Name(name)
        if self.__has_key(nm):
            return self.data[nm].add_phone(phone)
        raise KeyError

    def edit_phone(self, name, phone, new_phone):
        nm = Name(name)
        if self.__has_key(nm):
            return self.data[nm].edit_phone(phone, new_phone)
        raise KeyError

    def remove_phone(self, name, phone):
        nm = Name(name)
        if self.__has_key(nm):
            return self.data[nm].remove_phone(phone)
        raise KeyError

    def remove(self, name):
        nm = Name(name)
        if self.__has_key(nm):
            self.data.pop(nm)
            return "Record was removed."
        raise KeyError
    
    def add_email(self, name, email):
        nm = Name(name)
        if self.__has_key(nm):
            return self.data[nm].add_email(email)
        raise KeyError
    
    def edit_email(self, name, email):
        nm = Name(name)
        if self.__has_key(nm):
            return self.data[nm].edit_email(email)
        raise KeyError
    
    def show_email(self, name):
        nm = Name(name)
        if self.__has_key(nm):
            return self.data[nm].show_email()
        raise KeyError

    def add_address(self, name, address):
        nm = Name(name)
        if self.__has_key(nm):
            return self.data[nm].add_address(address)
        raise KeyError
    
    def edit_address(self, name, address):
        nm = Name(name)
        if self.__has_key(nm):
            return self.data[nm].edit_address(address)
        raise KeyError
    
    def show_address(self, name):
        nm = Name(name)
        if self.__has_key(nm):
            return self.data[nm].show_address()
        raise KeyError

    def add_birthday(self, name, birthday):
        nm = Name(name)
        if self.__has_key(nm):
            return self.data[nm].add_birthday(birthday)
        raise KeyError
    
    def edit_birthday(self, name, birthday):
        nm = Name(name)
        if self.__has_key(nm):
            return self.data[nm].edit_birthday(birthday)
        raise KeyError

    def show_birthday(self, name):
        nm = Name(name)
        if self.__has_key(nm):
            return self.data[nm].show_birthday()
        raise KeyError

    def get_birthdays_by_count_of_days(self, count_of_days):
        birthdays = defaultdict(list)
        current_year = datetime.datetime.today().year
        current_date = datetime.datetime.today().date()

        for value in self.data.values():
            if value.birthday is not None:
                name = value.name.value
                birthday = value.birthday.value
                birthday_this_year = (
                    birthday.replace(year=current_year)).date()

                if birthday_this_year < current_date:
                    birthday_this_year.replace(year=current_year + 1)

                delta_days = (birthday_this_year - current_date).days
                if delta_days < count_of_days and delta_days > 0:
                    day = AddressBook.__get_day(value.birthday.value)

                    if day in ("Saturday", "Sunday"):
                        day = "Monday"

                    birthdays[day].append(name)
        txt = ""
        for k, v in birthdays.items():
            txt += f"{k}: {'; '.join(n for n in v)}\n"
        return txt

    def exit(self):
        self.__save_to_file()
        sys.exit()

    def __get_day(date):
        return date.strftime("%A")

    def __has_key(self, value):
        return value in self.data.keys()

    def __getstate__(self):
        return self.data

    def __setstate__(self, value):
        self.data = value

    def __str__(self):
        return ("Address Book:\n"
                + '\n'.join([f'{value}' for value in self.data.values()]))


class Notes(UserDict):
    __file_name = "notes.bin"
    __path = os.path.join(os.getcwd(), __file_name)
    def __init__(self, name):
        super().__init__()
        self.name = name

        if os.path.isfile(self.__path) and os.path.getsize(self.__path) > 0:
            self.data = self.__read_from_file()
        else:
            self.data = {}

    def __save_to_file(self):
        with open(self.__path, "wb") as file:
            pickle.dump(self.data, file)

    def exit(self):
        self.__save_to_file()

    def __read_from_file(self):
        with open(self.__path, "rb") as file:
            return pickle.load(file)

    def __str__(self):
        return f'{self.name}'
    
    def update(self, other):
        if isinstance(other, dict):
            for key, value in other.items():
                self[key] = value
        else:
            for key, value in other:
                self[key] = value
        return self
    

class NoteHelper:
    def __init__(self, notes: Notes):
        self.notes = notes

    def make_note(self):
        named_note = input("What's the note's name? >>> ").rstrip()
        if named_note == '':
            return 'Name your note.'
        else:
            print(f"\n<{named_note}> created!\nYou can type now.\n(When finished, type 'close' in a new line):\n")
            lines = []
            while True:
                line = input()
                if line in ['close', 'exit', 'finish', 'done', 'save']:
                     break
                lines.append(line)
        print(f'\n({named_note}) - saved!\n')
        return {f'{named_note}':lines}

    def edit_note(self, name):
        print(f"<Editing <{name}>...\nYou can type now.\n(When finished, type 'close' in a new line):\n")
        lines = []
        while True:
            line = input()
            if line in ['close', 'exit', 'finish', 'done', 'save']:
                break
            lines.append(line)
        print(f'\n({name}) - saved!\n')
        return lines
    
    def all_notes(self):
        for key in self.notes.keys():
            print(f'-  {key}')
    
    def delete_note(self, name):
        confirmation = input('Do you want to delete? y/n ')
        if confirmation == 'y':
            self.notes.pop(name)
            print('Deleting...\nDone!')

        elif confirmation == 'n':
            print('Abort the mission!')

        else:
            print('Invalid answer (must be "y" or "n").')
        return ''
