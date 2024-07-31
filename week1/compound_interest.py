# compound interest
#  p = principle amount
#  r = rate
#  t = time
#  n = number of times interest is compounded per time period
def compoundInterest(p, r, t, n = 1):
    return p * (1 + r / n) ** (n * t)


# get input
principle = float(input("Enter the principle amount: "))
rate = float(input("Enter the rate of interest: "))
time = float(input("Enter the time in years: "))


total = compoundInterest(principle, rate, time)

print("The total amount is: ", total)
