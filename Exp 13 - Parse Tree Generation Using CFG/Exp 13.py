from nltk import CFG
from nltk.parse import ChartParser

grammar = CFG.fromstring("""
S -> NP VP
NP -> Det N
VP -> V NP
Det -> 'The' | 'the'
N -> 'boy' | 'girl'
V -> 'loves'
""")

parser = ChartParser(grammar)

sentence = "The boy loves the girl".split()

for tree in parser.parse(sentence):
    print(tree)
    print("\nTree Structure:\n")
    tree.pretty_print()
