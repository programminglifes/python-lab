def has_dublicates(lst):
    return len(lst) != len(set(lst))

length = int(input("Enter the length of list: "))

lst = []

for i in range(length):
    num = int(input("Enter the number: "))
    lst.append(num)

if has_dublicates(lst):
    print("List has dublicates")
else:
    print("List has no dublicates")
