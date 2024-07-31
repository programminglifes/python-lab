import array

def to_array(type: str):
    arr = array.array(type, [1, 2, 3, 4, 5])
    return arr

lst = [4, 5, 9, 10]

print("list: ", lst, "\n type: ", type(lst))

tpl = (15, 20, 130)

print("tuple: ", tpl, "\n type: ", type(tpl))

# converting tuple to array
arrFromArr = array.array("i", tpl)

print("array: ", arrFromArr, "\n type: ", type(arrFromArr))

# converting list to array
arrFromList = array.array("i", lst)

print("array: ", arrFromList, "\n type: ", type(arrFromList))
