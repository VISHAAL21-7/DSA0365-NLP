def pluralize(noun):
    if noun.endswith(('s', 'x', 'z', 'ch', 'sh')):
        return noun + "es"
    elif noun.endswith('y') and noun[-2] not in "aeiou":
        return noun[:-1] + "ies"
    else:
        return noun + "s"

nouns = ["cat", "bus", "box", "baby", "church"]

print("Singular\tPlural")
print("-" * 25)

for noun in nouns:
    print(f"{noun}\t\t{pluralize(noun)}")
