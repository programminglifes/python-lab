def gcd(val1, val2):
    if val1 < val2:
        val1, val2 = val2, val1
    while val1 % val2 != 0:
        rem = val1 % val2
        val1 = val2
        val2 = rem
    return val2


val1 = int(input("Enter the first number: "))
val2 = int(input("Enter the second number: "))

print("GCD of", val1, "and", val2, "is", gcd(val1, val2))
