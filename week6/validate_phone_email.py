def validate_phone(num: int):
    numA = str(num)
    length = len(numA)
    if length == 10:
        print("number is valid")
    else:
        print("number is invalid")


def validate_email(email: str):
    # user.name@domain.co.in
    # [ "user.name", "@", "domain", ".", "com" ]
    a = [""]
    current = 0
    for letter in email:
        if letter == "@":
            a.append(letter)
            a.append("")
            current += 2
        elif letter == ".":
            if "@" in a:
                a.append(letter)
                a.append("")
                current += 2
            else:
                a[current] = a[current] + "."
        else:
            a[current] = a[current] + letter
    
    if len(a) >= 5:
        print("email is not valid")
    if len(a[0]) == 0:
        print("email is not valid")
    elif a[1] != "@":
        print("email is not valid")
    elif a[3] != ".":
        print("email is not valid")
    else:
        print("email is valid")


number = int(input("Enter an Indian phone number without +91: "))
email = input("Enter a email: ")


validate_phone(number)
validate_email(email)
