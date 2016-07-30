#Alphabetical order checking function.
def alphabetOrder(word):
    if word == ''.join(sorted(word)):
        word += ' is in alphabetical order.'
    else:
        word += ' is not in alphabetical order.'
    return word

print(alphabetOrder(input(str("Input a word: "))))
