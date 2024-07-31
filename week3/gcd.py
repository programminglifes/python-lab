def gcd(val1, val2):
    if val1 == 0 and val2 == 0:
        return 0
    elif val1 == 0:
        return val2
    elif val2 == 0:
        return val1
    else:
        return gcd(val2, val1 % val2)


val1 = int(input("Enter the first number: "))
val2 = int(input("Enter the second number: "))

print("GCD of", val1, "and", val2, "is", gcd(val1, val2))
