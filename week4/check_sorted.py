def is_sorted(lst):
    for i in range(len(lst) - 1):
        if lst[i] > lst[i + 1]:
            return False
    return True

length = int(input("Enter the length of list: "))
lst = []
for i in range(length):
    num = int(input("Enter the number: "))
    lst.append(num)

if is_sorted(lst):
    print("List is sorted")
else:
    print("List is not sorted")
