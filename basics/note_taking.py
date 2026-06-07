##this is a program to take notes and display them
is_running = True
#list to store notes
notes = []

while is_running:
    print("Welcome to notes taking. Press q to exit")
    note = input("Enter your note:")
#to exit the program even if user types caps Q
    if note.lower() == "q":
        is_running = False
        break

    notes.append(note)

for note in notes:
    print(note)