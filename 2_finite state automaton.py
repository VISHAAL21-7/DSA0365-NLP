def fsa_ends_with_ab(string):
    state = 0
    for char in string:
        if state == 0:
            state = 1 if char == 'a' else 0
        elif state == 1:
            state = 2 if char == 'b' else (1 if char == 'a' else 0)
        elif state == 2:
            state = 1 if char == 'a' else 0
    return state == 2

print(fsa_ends_with_ab("aaab"))  # True