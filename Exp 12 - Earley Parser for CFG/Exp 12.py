from nltk import CFG
from nltk.parse import EarleyChartParser

grammar = CFG.fromstring("""
S -> NP VP
NP -> 'I'
VP -> 'run'
""")

parser = EarleyChartParser(grammar)

sentence = "I run".split()

for tree in parser.parse(sentence):
    print(tree)
