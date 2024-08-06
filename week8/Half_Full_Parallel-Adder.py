def half_adder(a, b):
    sum_ha = a ^ b
    carry_ha = a & b
    return sum_ha, carry_ha

def full_adder(a, b, c):
    sum_fa = (a ^ b) ^ c
    carry_fa = (a & b) | (b & c) | (c & a)
    return sum_fa, carry_fa

def parallel_adder(a_bits, b_bits):
    result = []
    carry = 0
    for i in range(len(a_bits) - 1, -1, -1):
        sum_fa, carry_fa = full_adder(a_bits[i], b_bits[i], carry)
        result.append(sum_fa)
        carry = carry_fa
    result.reverse()
    return result

def main():
    print("Digital Adder Implementation")
    print("---------------------------")

    # Half Adder
    print("Half Adder")
    a_ha = int(input("Enter first input (0/1): "))
    b_ha = int(input("Enter second input (0/1): "))
    sum_ha, carry_ha = half_adder(a_ha, b_ha)
    print(f"A = {a_ha}, B = {b_ha}")
    print(f"Sum = {sum_ha}, Carry = {carry_ha}")

    # Full Adder
    print("\nFull Adder")
    a_fa = int(input("Enter first input (0/1): "))
    b_fa = int(input("Enter second input (0/1): "))
    c_fa = int(input("Enter carry input (0/1): "))
    sum_fa, carry_fa = full_adder(a_fa, b_fa, c_fa)
    print(f"A = {a_fa}, B = {b_fa}, C = {c_fa}")
    print(f"Sum = {sum_fa}, Carry = {carry_fa}")

    # Parallel Adder
    print("\nParallel Adder")
    num_bits = int(input("Enter number of bits: "))
    a_bits = []
    b_bits = []
    for i in range(num_bits):
        a_bit = int(input(f"Enter bit {i} of A (0/1): "))
        b_bit = int(input(f"Enter bit {i} of B (0/1): "))
        a_bits.append(a_bit)
        b_bits.append(b_bit)
    result = parallel_adder(a_bits, b_bits)
    print(f"A = {a_bits}, B = {b_bits}")
    print(f"Result = {result}")

if __name__ == "__main__":
    main()
