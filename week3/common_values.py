
def commonValues(lst1, lst2):
    common = []
    for i in lst1:
        for j in lst2:
            if i == j:
                common.append(i)
    return set(common)

lst1 = []
lst2 = []

n1 = int(input("Enter the size of list1: "))

for i in range(n1):
    num = int(input("Enter the number: "))
    lst1.append(num)

n2 = int(input("Enter the size of list2: "))

for i in range(n2):
    num = int(input("Enter the number: "))
    lst2.append(num)

print("Common values in both list: ", commonValues(lst1, lst2))
