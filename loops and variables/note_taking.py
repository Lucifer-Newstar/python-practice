is_running = True
notes = []

while is_running:
    print("Welcome to notes taking. Press q to exit")
    note = input("Enter your note:")

    if note.lower() == "q":
        is_running = False
        break

    notes.append(note)

for note in notes:
    print(note)