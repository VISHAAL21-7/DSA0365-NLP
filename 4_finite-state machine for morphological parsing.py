def pluralize(noun):
    if noun.endswith('y'):
        return noun[:-1] + 'ies'
    elif noun.endswith(('s', 'x', 'z', 'ch', 'sh')):
        return noun + 'es'
    else:
        return noun + 's'

print(pluralize("suck"))
print("a")
print(pluralize("baby"))
print(pluralize("box"))