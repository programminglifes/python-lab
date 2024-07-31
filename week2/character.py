def charType(character: str):
    ascii = ord(character)
    if ascii >= 40 and ascii <= 57:
        return "Number"
    elif ascii >= 65 and ascii <= 90:
        return "Capital Letters"
    elif ascii >= 97 and ascii <= 122:
        return "Small Letter"
    else:
        return "Special Character"


data = input("Enter any character: ")

print("The type of character is:", charType(data))
