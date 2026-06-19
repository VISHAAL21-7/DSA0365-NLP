import nltk
from nltk import PCFG
from nltk.parse import ViterbiParser

grammar = PCFG.fromstring("""
S -> NP VP [1.0]
NP -> 'John' [0.5] | 'Mary' [0.5]
VP -> 'runs' [1.0]
""")

parser = ViterbiParser(grammar)

for tree in parser.parse("John runs".split()):
    print(tree)
