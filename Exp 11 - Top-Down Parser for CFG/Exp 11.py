# Grammar:
# S -> aSb | ab

def parse(string):
    if string == "ab":
        return True

    if len(string) >= 2 and string[0] == 'a' and string[-1] == 'b':
        return parse(string[1:-1])

    return False

s = input("Enter a string: ")

if parse(s):
    print("Accepted")
else:
    print("Rejected")
