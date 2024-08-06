def AND(a, b):
    return a & b

def OR(a, b):
    return a | b

def NOT(a):
    return ~a + 2

def EXOR(a, b):
    return a ^ b

def main():
    print("Digital Logic Gates Implementation")
    print("-----------------------------------")

    # Input values
    a = int(input("Enter first input (0/1): "))
    b = int(input("Enter second input (0/1): "))

    # Validate input values
    if a not in [0, 1] or b not in [0, 1]:
        print("Invalid input. Please enter 0 or 1.")
        return

    # Perform logic gate operations
    and_result = AND(a, b)
    or_result = OR(a, b)
    not_a_result = NOT(a)
    not_b_result = NOT(b)
    exor_result = EXOR(a, b)

    # Display results
    print(f"A = {a}, B = {b}")
    print(f"AND (A, B) = {and_result}")
    print(f"OR (A, B) = {or_result}")
    print(f"NOT A = {not_a_result}")
    print(f"NOT B = {not_b_result}")
    print(f"EX-OR (A, B) = {exor_result}")

if __name__ == "__main__":
    main()
