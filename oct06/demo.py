from matplotlib import pyplot as plt
import nltk
import random

text = """
To Sherlock Holmes she is always _the_ woman. I have seldom heard him
mention her under any other name. In his eyes she eclipses and
predominates the whole of her sex. It was not that he felt any emotion
akin to love for Irene Adler. All emotions, and that one particularly,
were abhorrent to his cold, precise but admirably balanced mind. He
was, I take it, the most perfect reasoning and observing machine that
the world has seen, but as a lover he would have placed himself in a
false position. He never spoke of the softer passions, save with a gibe
and a sneer. They were admirable things for the observer—excellent for
drawing the veil from men’s motives and actions. But for the trained
reasoner to admit such intrusions into his own delicate and finely
adjusted temperament was to introduce a distracting factor which might
throw a doubt upon all his mental results. Grit in a sensitive
instrument, or a crack in one of his own high-power lenses, would not
be more disturbing than a strong emotion in a nature such as his. And
yet there was but one woman to him, and that woman was the late Irene
Adler, of dubious and questionable memory.
"""

def tokenize(string):
    tokens = []
    i = 0
    token = ""
    while string != "":
        if string[0] == " ":
            tokens.append(token)
            token = ""
        else:
            token += string[0]
        string = string[1:]

    return tokens      

def readFile(name):
    with open(name, "r") as textFile:
        text = textFile.read()
        return text

def start():
    
    text = readFile("sherlock.txt")
    
    tokens = nltk.word_tokenize(text)
    
    words_pos = nltk.pos_tag(tokens)
    
#    print(words_pos)
 
    pos = []
    for item in words_pos:
        if item[1] == "NN":
            print(item[0])

if __name__ == "__main__":
    start()









