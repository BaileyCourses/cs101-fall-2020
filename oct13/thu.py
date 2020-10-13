from matplotlib import pyplot as plt
import nltk
import random

text = """
Most of the adventures recorded in this book really occurred; one or two
were experiences of my own, the rest those of boys who were schoolmates
of mine. Huck Finn is drawn from life; Tom Sawyer also, but not from an
individual--he is a combination of the characteristics of three boys whom
I knew, and therefore belongs to the composite order of architecture.
"""

newNames = [
    "David Wippman",
    "Donald Trump",
    "Mike Pence",
    "Kamala Harris",
    "Joe Biden",
    "Eddie Van Halen",
    "Matt Levine",
    "Jim Dwyer",
    "Louise Gluck",
    "Maya Wiley",
    "Vladimir Putin",
    "Laurie Santos",
    "LeBron James",
    "Jimmy Kimmel"
    "Paul Abernathy"
    ]

def readFile(name):
    with open(name, "r") as textFile:
        text = textFile.read()
        return text

def start():
    print("Reading file...")
    text = readFile("tom-sawyer.txt")
    
    names = findPopularProperNouns(text)
    
    sents = nltk.sent_tokenize(text)

    colocations = set()
    for sent in sents:
        print(sent)
        nouns = set()
        for name in names:
            pass
#            if name in sent:
#                nouns.add(name)
#        colocations.add(nouns)
        
    print(colocations)
            

def findPopularProperNouns(text, size = 20):
    words = nltk.word_tokenize(text)        # Break the work up into words

    words_pos = nltk.pos_tag(words)     # Find parts of speach for each word
    
    names = []

    for (word, pos) in words_pos:
        if (pos == "NNP" or pos == "NNPS") and len(word) > 1:
            addCounts(names, word)

    names = sorted(names, reverse = True)[:size]
    
    return names
               

def addCounts(counts, word):
    for i in range(len(counts)):
        if counts[i][1] == word:
            counts[i][0] += 1
            return
    counts.append([1, word])

if __name__ == "__main__":
    start()









