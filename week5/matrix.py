def getMatrix():
    rows = int(input("Enter the number of rows: "))
    cols = int(input("Enter the number of cols: "))

    matrix = []

    for i in range(rows):
        row = []
        for j in range(cols):
            row.append(int(input(f"element at {i} row {j} col: ")))
        matrix.append(row)

    return matrix

def printMatrix(matrix: list):
    print() # this will add an empty line before printing the matrix
    for row in matrix:
        for element in row:
            print(element, end="\t")
        print()
    print() # this will add an empty line after printing the matrix

def addMatrix(mat1, mat2):

    if len(mat1) != len(mat2):
        print("matrix 1 and matrix 2 do not have the same number of rows")
        return []

    if len(mat1[0]) != len(mat2[0]):
        print("matrix 1 and matrix 2 do not have the same number of cols")
        return []

    newMat = []
    for i in range(len(mat1)):
        row = []
        for j in range(len(mat1[i])):
            row.append(mat1[i][j] + mat2[i][j])
        newMat.append(row)

    return newMat

def mulMatrix(mat1, mat2):
    if len(mat1[0]) != len(mat2):
        print("matrix 1 and matrix 2 do not have the same number of cols")
        return []

    newMat = []
    for i in range(len(mat1)):
        row = []
        for j in range(len(mat2[0])):
            sum = 0
            for k in range(len(mat2)):
                sum += mat1[i][k] * mat2[k][j]
            row.append(sum)
        newMat.append(row)

    return newMat

mat1 = getMatrix()
mat2 = getMatrix()
printMatrix(mat1)
printMatrix(mat2)

sum = addMatrix(mat1, mat2)
printMatrix(sum)
mult = mulMatrix(mat1, mat2)
printMatrix(mult)
