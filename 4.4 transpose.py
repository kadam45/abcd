# Transpose of a matrix
row = int(input("Enter the number of rows:"))
col = int(input("Enter the number of columns:"))
a = []
# Initialize matrix
matrixa = []
matrixb = []
result = []

print("Enter the entries rowwise:")

# For user input
for i in range(row):  # A for loop for row entries
    a = []
    for j in range(col):  # A for loop for column entries
        a.append(int(input()))
    matrixa.append(a)

# For printing matrix
for i in range(row):
    for j in range(col):
        print(matrixa[i][j], end=" ")
    print()
    # result matrix

for i in range(col):
    a = []
    for j in range(row):
        a.append(0)
    result.append(a)
'''
for i in range(col):
    for j in range(row):
        print(result[i][j], end=" ")
    print()
'''
# transpose of matrix
for i in range(row):
    for j in range(col):
        result[j][i] = matrixa[i][j]

# print result
print("Result matrix for transpose of matrix is:")
for i in range(col):
    for j in range(row):
        print(result[i][j], end=" ")
    print()

