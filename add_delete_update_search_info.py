from datetime import datetime, timedelta

class Record:
    def __init__(self):
        self.contacts = []

    def add_contact(self, name, phone, address=None, email=None, birthday=None):
        # Перевірка, чи контакт з таким ім'ям вже існує
        for contact in self.contacts:
            if contact["name"] == name:
                update_choice = input("Contact already exists. Do you want to update it? (yes/no): ").lower()
                if update_choice == "yes":
                    # Виклик методу для оновлення контакту
                    return self.update_contact(name, phone, address, email, birthday)
                else:
                    return "Contact not added. Returning to main menu."

        # Додавання нового контакту, якщо він не існує
        contact = {"name": name, "phone": phone, "address": address, "email": email, "birthday": birthday}
        self.contacts.append(contact)
        return "Contact added."

    def search_contact(self, name):
        for contact in self.contacts:
            if contact["name"] == name:
                return contact
        return None

    def update_contact(self, name, phone=None, address=None, email=None, birthday=None):
        # Пошук контакту за іменем
        for contact in self.contacts:
            if contact["name"] == name:
                # Оновлення інформації про контакт
                if phone:
                    contact["phone"] = phone
                if address:
                    contact["address"] = address
                if email:
                    contact["email"] = email
                if birthday:
                    contact["birthday"] = birthday
                return "Contact updated."

        # Повідомлення про те, що контакт не знайдено
        return "Contact not found."

    def delete_contact(self, name):
        # Пошук та видалення контакту
        for contact in self.contacts:
            if contact["name"] == name:
                self.contacts.remove(contact)
                return f"Contact {name} deleted."
        return "Contact not found."

    def show_all_contacts(self):
        # Вивід усіх контактів
        if not self.contacts:
            return "No contacts found."
        else:
            for contact in self.contacts:
                print(f"Name: {contact['name']}, Phone: {contact['phone']}, Address: {contact.get('address', 'N/A')}, Email: {contact.get('email', 'N/A')}, Birthday: {contact.get('birthday', 'N/A')}")

def parse_input(user_input):
    parts = user_input.strip().split(maxsplit=1)
    command = parts[0].lower()
    args = parts[1] if len(parts) > 1 else ""
    return command, args

def main():
    book = Record()
    print("Welcome to the assistant bot!")

    while True:
        user_input = input("Enter a command: ")
        command, args = parse_input(user_input)

        if command == "exit" or command == "close":
            print("Goodbye!")
            break
        elif command == "hello":
            print("How can I help you?")
        elif command == "add":
            info = args.split()
            if len(info) < 2:
                print("Invalid number of arguments. Usage: add [name] [phone] [address (optional)] [email (optional)] [birthday (optional)]")
            else:
                name = info[0]
                phone = info[1]
                address = info[2] if len(info) > 2 else None
                email = info[3] if len(info) > 3 else None
                birthday = info[4] if len(info) > 4 else None
                print(book.add_contact(name, phone, address, email, birthday))
        elif command == "search":
            if not args:
                print("Invalid number of arguments. Usage: search [name]")
            else:
                contact = book.search_contact(args)
                if contact:
                    print(f"Contact found: {contact}")
                else:
                    print("Contact not found.")
        elif command == "update":
            info = args.split()
            if len(info) < 2:
                print("Invalid number of arguments. Usage: update [name] [attribute=value]...")
            else:
                name = info[0]
                kwargs = {}
                for item in info[1:]:
                    key, value = item.split("=")
                    kwargs[key] = value
                print(book.update_contact(name, **kwargs))
        elif command == "delete":
            if not args:
                print("Invalid number of arguments. Usage: delete [name]")
            else:
                print(book.delete_contact(args))
        elif command == "all":
            book.show_all_contacts()
        else:
            print("Invalid command.")

if __name__ == "__main__":
    main()
