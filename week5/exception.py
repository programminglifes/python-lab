try:
    raise Exception("I am an exception")
except Exception as e:
    print(e)
    print("you successfully handled the error")


try:
    print(x)
except NameError as e:
    print(e)
except:
    print("Something else went wrong")

try:
    x = 1
    x = x + "super"
except TypeError:
    print("Type error is now handled")


raise Exception("An exception is raised, the program will now exit")

# This is now unreachable code
print("I am unreachable code")
