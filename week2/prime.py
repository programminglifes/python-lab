
def prime(start, stop):
    primes = []
    for i in range(start, stop+1):
        if i > 1:
            for j in range(2, i):
                if (i % j) == 0:
                    break
            else:
                primes.append(i)
    return primes

start = int(input("Enter the starting number: "))
stop = int(input("Enter the ending number: "))

print("Prime numbers between", start, "and", stop, "are: ", end="")

print(prime(start, stop))
