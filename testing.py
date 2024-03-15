from prompt_toolkit import PromptSession
from prompt_toolkit.completion import WordCompleter


notes = {
    "note1": "Hello Peppo!n",
    "nottierre": "Contentofnote",
    "notta": "Content of note 3",
    "noticable 123123           234": "Content of note 1",
    "note2": "Content of note 2",
    "note222": "Content of note 3",
    "note the goose": "Content of note 1",
    "noughty dog": "Content of note 2",
    "notesaf": "Content of note 3",
    "note234234": "Content of note 1",
    "noteaaaaaaaaa": "Content of note 2",
    "note3aaaa": "Content of note 3"
}


completer = WordCompleter(notes.keys())


session = PromptSession()


def open_note():
    note_name = session.prompt("Enter note name: ", completer=completer)

    if note_name in notes:
        print("Note content:", notes[note_name])
    else:
        print(f"No such note ({note_name}) exists.")


open_note()
