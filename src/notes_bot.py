# from prompt_toolkit import PromptSession
# from prompt_toolkit.completion import WordCompleter
from src.models import Notes
from src.models import NoteHelper


def open_notes():
    my_notes = Notes("my_notes")
    helper = NoteHelper(my_notes)
    while True:
        try:
            user_input = input("What is your Notes command? >>> ")
            command, *args = user_input.split()
            command = command.strip().lower()
            
            if command in ['close', 'exit', 'finish', 'done']:
                print('Exiting Notes...\nAssistant listening...')
                break
            elif command == 'make-note':
                new_note = helper.make_note()
                my_notes.update(new_note)
            elif command == 'open-note':
                try:
                    note_name = args[0]
                    if note_name in my_notes:
                        print(f'Opening note: {note_name}\n')
                        print(f'_________________{note_name}_________________\n')
                        for line in my_notes[note_name]:
                            print(line)
                        print(f'\n_________________{note_name}_________________\n')
                    else:
                        print(f'No such note ({args}) exists.')
                except:
                    print('You need to type the name of the note.')
            elif command == 'edit-note':
                try:
                    note_name = args[0]
                    if note_name in my_notes:
                        print(f'Opening note to edit: {note_name}\n')
                        print(f'_________________{note_name}_________________\n')
                        for line in my_notes[note_name]:
                            print(line)
                        print(f'_________________{note_name}_________________\n')
                        new_note = helper.edit_note(note_name)
                        my_notes[note_name] = new_note
                except:
                    print('You need to type the correct name of the note.')
                else:
                    print(f'No such note ({new_note}) exists.')
            elif command == 'delete-note':
                try:
                    note_name = args[0]
                    if note_name in my_notes:
                        print(helper.delete_note(note_name))
                except:
                    print(f'No such note ({note_name}) exists.')
            elif command == 'all-notes':
                try:
                    print('____________________________\n')
                    for key in my_notes.keys():
                        print(key)
                    print('____________________________\n')
                except:
                    print('No available notes.\n\n')
            else:
                print("\n\nChoose a command from the list below:\n")
                print("{:<15} + {:^20} -- {:<25}".format('make-note', '~', 'create a new note'))
                print("{:<15} + {:^20} -- {:<25}".format('open-note', '<note name>', 'open a note by name'))
                print("{:<15} + {:^20} -- {:<25}".format('edit-note', '<note name>', 'edit a note by name'))
                print("{:<15} + {:^20} -- {:<25}".format('all-notes', '~', 'check all the notes by name'))
                print("{:<15} + {:^20} -- {:<25}".format('delete-note', '<note name>', 'delete a note by name\n\n'))
        except ValueError:
            print('You need to type something.')
    return my_notes