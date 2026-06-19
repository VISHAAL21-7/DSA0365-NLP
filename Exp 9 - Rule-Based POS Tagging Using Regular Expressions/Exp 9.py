import re

words = ["running", "played", "cats", "beautiful", "quickly"]

print("{:<15}{:<10}".format("Word", "POS Tag"))
print("-" * 25)

for word in words:
    if re.search(r'ing$', word):
        tag = "VBG"  
    elif re.search(r'ed$', word):
        tag = "VBD"   
    elif re.search(r'ly$', word):
        tag = "RB"    
    elif re.search(r'ful$', word):
        tag = "JJ"    
    elif re.search(r's$', word):
        tag = "NNS"   
    else:
        tag = "NN"    

    print("{:<15}{:<10}".format(word, tag))
