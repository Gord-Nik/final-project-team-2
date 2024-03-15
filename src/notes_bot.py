from prompt_toolkit import PromptSession
from prompt_toolkit.completion import WordCompleter
from src.models import Notes
from src.models import NoteHelper


my_notes = Notes("my_notes")


def check_args_length(args):
    if len(args) < 1:
        raise ValueError


def open_notes():

    helper = NoteHelper(my_notes)
    command_list = ['make-note',
                    'open-note',
                    'edit-note',
                    'delete-note',
                    'all-notes',
                    'close',
                    'exit',
                    'finish',
                    'done',
                    'add-tag']
    session = PromptSession()
    while True:
        combined_list = command_list + list(my_notes.keys())
        completer = WordCompleter(combined_list)
        try:
            user_input = session.prompt("What is your Notes command? >>> ", completer=completer)
            command, *args = user_input.split()
            command = command.strip().lower()
            
            if command in ['close', 'exit', 'finish', 'done']:
                print('Exiting Notes...\nAssistant listening...')
                my_notes.exit()
                
                break

            elif command == 'make-note':
                new_note = helper.make_note()
                my_notes.update(new_note)

            elif command == 'open-note':
                check_args_length(args)

                try:
                    note_name = args[0]
                    if note_name in my_notes:
                        print(f'Opening note: {note_name}\n')

                        print(f'_________________{note_name}_________________\n')
                        for line in my_notes[note_name].text:
                            print(line)
                        print(f'\n_________________{note_name}_________________\n')

                        print("tags:")
                        for line in my_notes[note_name].tags:
                            print(line)
                    else:
                        print(f'No such note ({args}) exists.')
                except:
                    print('You need to type the name of the note.')

            elif command == 'edit-note':
                check_args_length(args)

                try:
                    note_name = args[0]
                    if note_name in my_notes:
                        print(f'Opening note to edit: {note_name}\n')
                        print(f'_________________{note_name}_________________\n')
                        for line in my_notes[note_name].text:
                            print(line)
                        print(f'_________________{note_name}_________________\n')
                        new_note = helper.edit_note(note_name)
                        my_notes[note_name].text = new_note
                except:
                    print('You need to type the correct name of the note.')
                else:
                    print(f'No such note ({new_note}) exists.')

            elif command == 'delete-note':
                check_args_length(args)

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

            elif command == 'add-tag':
                name, tag = args
                helper.add_tag_to_note(name, tag)

            elif command == 'find-notates-by-tag':
                check_args_length(args)

                tag = args[0]
                notes = helper.find_notates_by_tag(tag)

                print('____________________________\n')
                for note in notes:
                    print(note)
                print('____________________________\n')

            else:
                print("\n\nChoose a command from the list below:\n")
                print("{:<15} + {:^20} -- {:<25}".format('make-note', '~', 'create a new note'))
                print("{:<15} + {:^20} -- {:<25}".format('open-note', '<note name>', 'open a note by name'))
                print("{:<15} + {:^20} -- {:<25}".format('edit-note', '<note name>', 'edit a note by name'))
                print("{:<15} + {:^20} -- {:<25}".format('all-notes', '~', 'check all the notes by name'))
                print("{:<15} + {:^20} -- {:<25}".format('delete-note', '<note name>', 'delete a note by name'))
                print("{:<15} + {:^20} -- {:<25}".format('add-tag', '<note name>, <note tag>', 'add tag to the node\n\n'))
        except ValueError:
            print('You need to type something.')
    return my_notes