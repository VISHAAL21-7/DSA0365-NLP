dialog = input("Enter a dialog: ")

if dialog.endswith("?"):
    print("Dialog Act: Question")
elif dialog.lower().startswith(("hello", "hi", "good morning")):
    print("Dialog Act: Greeting")
else:
    print("Dialog Act: Statement")
