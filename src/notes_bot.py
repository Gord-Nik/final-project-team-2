from src.models import Notes
from src.models import NoteHelper







def open_notes():
    my_notes = Notes("my_notes")
    helper = NoteHelper(my_notes)
    while True:
        user_input = input("What is your Notes command? >>> ")
        command, *args = user_input.split()
        command = command.strip().lower()

        if command in ['close', 'exit', 'finish', 'done']:
            print('Exiting Notes...')
            break
        elif command == 'make-note':
            my_notes.update(helper.make_note())
            print('Note is successfully added.')
        elif command == 'open-note':
            if args in my_notes:
                print(helper.open_note(args))
            else:
                print(f'No such note ({args}) exists.')
        elif command == 'edit-note':
            if args in my_notes:
                print(f"The note ({helper.edit_note(args)}) has been edited")
            else:
                print(f'No such note ({args}) exists.')
        elif command == 'delete-note':
            if args in my_notes:
                print(helper.delete_note(args))
            else:
                print(f'No such note ({args}) exists.')
        elif command == 'all-notes':
            print(helper.all_notes())
        else:
            print("Choose a command from the list below:")
            print("{:<15} + {:^20} --> {:<25}".format('make-note', '~', 'create a new note'))
            print("{:<15} + {:^20} --> {:<25}".format('open-note', '<note name>', 'open a note by name'))
            print("{:<15} + {:^20} --> {:<25}".format('edit-note', '<note name>', 'edit a note by name'))
            print("{:<15} + {:^20} --> {:<25}".format('all-notes', '~', 'check all the notes by name'))
            print("{:<15} + {:^20} --> {:<25}".format('delete-note', '<note name>', 'delete a note by name'))
    return my_notes