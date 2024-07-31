
def fibonacchi(first, second, count):
    index = 0
    list = [first, second]
    while index < count:
        next = first + second
        list.append(next)
        first = second
        second = next
    return list


count = int(input("Enter your desired quantity: "))

print("Fibonacchi series is:\n", fibonacchi(0, 1, count))
