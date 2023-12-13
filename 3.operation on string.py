

#To display word with the longest length
str1=input("Enter the string To display word with the longest length: \n")
# svpm coe malegaon
list1=str1.split()     
m=0
word=0
print(list1)    
for i in range(len(list1)):
    if m<len(list1[i]):        
        m=len(list1[i])
        word=i
print("The word with longest length:- ",list1[word])




# To determines the frequency of occurrence of particular character in the string
str1 = input("Enter the string to count frequency of occurrence of particular character: \n")

char = input("Enter character:- ")

counter = 0
for i in range(len(str1)):     
    if char == str1[i]:         
        counter += 1
print("Character ",char," is present ",counter," times in string ",str1)


# To count the occurrences of each word in a given string
str1 = input("Enter input string To count the occurrences of each word: \n")

list1 = str1.split()

list2 = set(list1)  
list3 = list(list2)  

print(list1) 
print(list3) 

list4 = []
list5 = []
counter = 0
for i in range(len(list3)):
    counter = 0
    for j in range(len(list1)):     

        if list3[i] == list1[j]:
            counter += 1
    list4 = list3[i], counter
    list5.append(list4)
print("\n", list5)


# To check whether given string is palindrome or not
a = input("Enter string is palindrome or not: \n")  
c=a[ : :-1]          
if (c==a):
    print("string a is palindrome")
else:
    print("string a is not palindrome")

    

# To display index of first appearance of the substring
str1 = input("Enter the string To display index of first appearance of the substring:- \n")
sub1 = input("Enter substring:- \n")
index=str1.find(sub1)
sublen = len(sub1)
print("substring index :", index)