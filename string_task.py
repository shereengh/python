print("Mad libs where libs get Mad")
print(" Start Below:")
print("")
print("Enter the following: ")
time = input("Number: ")
items = input("Noun(plural): ")
name = input("Name: ")
name = name.title()
scream = input("Any sentence: ")
scream = scream.upper()
action = input("Verb: ")
print("""It was {} o'clock when I heard a knock at the door.
    I opened the door and there was a box full of {} with a note saying "From Mr. {}".
    Just as I closed the door I heard a scream "{}".
    I froze in place and all I could do was {}.
""".format(time, items, name, scream, action))