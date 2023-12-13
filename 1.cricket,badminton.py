# List holding names of students
groupA = ['Aman', 'Raj', 'Atharva', 'Ruchi']
groupB = ['Aman', 'Saloni', 'Aditya', 'Ayush', 'Atharva']
groupC = ['Raj','Ruchi', 'Vedant','Atharva']

#List of students who play both cricket and badminton
lena=len(groupA)
lenb=len(groupB)
print(" list of Students who play both cricket and badminton")
resultlistCB = []
for i in range(lenb):
    for var in range(lena):
        if(groupB[i]==groupA[var]):
            resultlistCB.append(groupB[i])
            break
print(resultlistCB)

# List of students who play both cricket and badminton.
# Alternative for above code.
"""print(" list of Students who play both cricket and badminton")
resultlistCB = []
if lena < lenb:
    for i in range(lena):
        for var in range(lenb):
            if (groupA[i] == groupB[var]):
                resultlistCB.append(groupA[i])
                break
else:
    for i in range(lenb):
        for var in range(lena):
            if (groupB[i] == groupA[var]):
                resultlistCB.append(groupB[i])
                break

print(resultlistCB)"""

# List of students who play either cricket or badminton but not both
print(" list of Students who play either cricket or badminton but not both")
resultlistCBN = []
flag = 0
if lena < lenb:
    for i in range(lenb):
        for var in range(lena):
            if (groupB[i] == groupA[var]):           #same
                flag = 1
        if (flag == 0):
            resultlistCBN.append(groupB[i])        #add different
        flag = 0


else:
    for i in range(lena):
        for var in range(lenb):
            if (groupA[i] == groupB[var]):
                flag = 1
        if (flag == 0):
            resultlistCBN.append(groupA[i])
        flag = 0

print(resultlistCBN)

#Number of students who play neither cricket nor badminton(only football)
print("Number of students who play neither cricket nor badminton")
resultlistCBNF = []
lenc=len(groupC)
for i in range(lenc):
    for var in range(lena):
        if(groupC[i]==groupA[var]):    #player from c  found in Group A
            flag=1
            break
    for var1 in range(lenb):            #player from c  found in Group B
        if(groupC[i]==groupB[var]):
            flag=1
            break
    if(flag==0):
        resultlistCBNF.append(groupC[i])    #player from c not found in Group A and B
    flag=0
print(resultlistCBNF)

#Number of students who play cricket and football but not badminton.
lena=len(groupA)
lenc=len(groupC)
print(" list of Students who play cricket and football but not badminton")
resultlistCF=[]
for i in range(lenc):
    for var in range(lena):
        if(groupC[i]==groupA[var]):
            resultlistCF.append(groupC[i])
            break
 #print(resultlistCF)  player play cricket and football
resultlistNB = []
flag = 0
lencf=len(resultlistCF)
for i in range(lencf):
    for var in range(lenb):
        if (resultlistCF[i] == groupB[var]):
             flag = 1
             break
    if (flag == 0):
            resultlistNB.append(resultlistCF[i])
    flag = 0
print(resultlistNB)      #player play cricket and football but not badminton


