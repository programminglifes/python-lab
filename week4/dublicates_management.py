def has_dublicates(lst):
    length = len(lst)
    for i in range(length):
        for j in range(i + 1, length):
            if lst[i] == lst[j]:
                return True
    return False

def remove_dublicates(lst):
    length = len(lst)
    for i in range(length):
        for j in range(i + 1, length):
            if lst[i] == lst[j]:
                lst.pop(j)
    return lst

def 

length = int(input("Enter the length of list: "))

lst = []

for i in range(length):
    num = int(input("Enter the number: "))
    lst.append(num)

if has_dublicates(lst):
    print("List has dublicates")
    print("List after removing dublicates: ", remove_dublicates(lst))
else:
    print("List has no dublicates")
