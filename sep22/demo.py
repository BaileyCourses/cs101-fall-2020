def start():
    
#    long = longer("Hello", "Goodbye")
#    long2 = longer("Cat", "Tiger")
    
#    print("The longer strings are", long, long2)
    
    #yesno = isVowel("u")
    #print(yesno)
    
#    numVowels = countVowels("Hello")
#    print(numVowels)

#    if not isVowel("r"):
#        print("It's a consonant")

#    if isVowel("e"):
#        print("It's a vowel")
#    print(countConsonants("consonant"))

#    print(max(34, 34))

#    print(hasDoubleLetter("aloha"))
    print(doubleLetters("doubledddoubledd"))
    
def doubleLetters(word):
    doubles = []
    for i in range(len(word) - 1):
        if word[i] == word[i + 1]:
            if word[i] not in doubles:
                doubles.append(word[i])

    return doubles
    
def hasDoubleLetter(word):
    for i in range(len(word) - 1):
        if word[i] == word[i + 1]:
            return True
    return False

def max(x, y):
    if x < y:
        return y
    return x

def countVowels(word):
    
    count = 0
    for letter in word:
        if isVowel(letter):
            count = count + 1

    return count

def countConsonants(word):
    return len(word) - countVowels(word)

def isVowel(letter):
    if letter == "a":
        return True
    if letter == "e":
        return True
    if letter == "i":
        return True
    if letter == "o":
        return True
    if letter == "u":
        return True

    return False

def longer(stringA, stringB):
    if len(stringA) < len(stringB):
        return stringB
    else:
        return stringA

if __name__ == "__main__":
    start()