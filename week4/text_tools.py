def comma(word: str):
    withComma = ""
    for i in word:
        withComma += i + ","
    return withComma[: len(word) * 2 - 1]


def splitByWord(text: str):
    textSplit = [""]
    current = 0
    for i in range(len(text)):
        if text[i] in [" ", ",", ".", ";", '"']:
            textSplit.append(text[i])
            textSplit.append("")
            current += 2
        else:
            textSplit[current] = textSplit[current] + text[i]
    return textSplit


def removeWord(text: str, word: str):
    textSplit = splitByWord(text)
    i = -1
    for j in textSplit:
        i += 1
        if j == word:
            textSplit.pop(i)

    return "".join(textSplit)


# without using default functions to convert to upper and lower case
def titleCase(text: str):
    textSplit = splitByWord(text)
    j = 0
    for word in textSplit:
        isFirst = True
        newWord = ""
        for i in range(len(word)):
            letter = word[i]
            ascii = ord(letter)
            finalLetter = ""
            # if capital
            if ascii >= 65 and ascii <= 90:
                if isFirst:
                    finalLetter = chr(ascii)
                else:
                    finalLetter = chr(ascii+32)
            # if small
            elif ascii >= 97 and ascii <= 122:
                if isFirst:
                    finalLetter = chr(ascii-32)
                else:
                    finalLetter = chr(ascii)
            else:
                finalLetter = chr(ascii)
            isFirst = False
            newWord += finalLetter
        textSplit[j] = newWord
        j += 1

    return "".join(textSplit)


word = input("enter your word ")
print(comma(word))

text = input("Enter your text: \n")
word = input("Enter the word you want to remove: ")
print(removeWord(text, word))
print(titleCase(text))
