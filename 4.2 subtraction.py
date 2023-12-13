# subtraction of two matrices
row = int(input("Enter the number of rows:"))
col = int(input("Enter the number of columns:"))

# Initialize matrix
matrixa = []
matrixb = []
resultmatrix = []
print("Enter the entries row wise:")

# For user input
print("Enter the entries for matrix A :\n")
for i in range(row):  # A for loop for row entries
    a = []
    for j in range(col):  # A for loop for column entries
        a.append(int(input()))
    matrixa.append(a)
print(matrixa)

# For printing first  matrix
print("First matrix :\n")
for i in range(row):
    for j in range(col):
        print(format(matrixa[i][j],"<3"), end=" ")
    print()

print("Enter entries for matrix B:\n")
for i in range(row):  # A for loop for row entries
    a = []
    for j in range(col):  # A for loop for column entries
        a.append(int(input()))
    matrixb.append(a)

# For printing second  matrix
print("Second matrix is:\n")
for i in range(row):
    for j in range(col):
        print(format(matrixb[i][j],"<3"), end=" ")
    print()

# For matrix subtraction
for i in range(row):
    a = []
    for j in range(col):
        a.append(matrixa[i][j] - matrixb[i][j])
    resultmatrix.append(a)

print("Subtraction of both matrix is:\n")
# For printing the result matrix
for i in range(row):
    for j in range(col):
        print(format(resultmatrix[i][j],"<3"), end=" ")
    print()

