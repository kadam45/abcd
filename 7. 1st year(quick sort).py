def partition(A,l,h) :
   pivot=A[l]
   i=l
   j=h
   while(i<=j) : 
      while(A[i]<=A[l]):
         i = i + 1                           
      while(A[j] >A[l]) :
         j = j - 1
      if(i<j) :
         temp = A[i]
         A[i] = A[j]
         A[j] = temp
   temp = A[l]
   A[l] = A[j]
   A[j]  = temp
   return j

def Quicksort(A,l,h) :
   if(l<h) :
      mid = partition(A,l,h)
      Quicksort(A,l,mid-1)
      Quicksort(A,mid+1,h)



A = []
print("****************************************************************Quick_Sort****************************************************************")
Num = int(input("Enter the number of students: "))
for i in range(Num):
    per = float(input("Enter the percentage marks: "))
    A.append(per)

Quicksort(A,0,Num-1)
print("Sorted array is:")
for i in range(len(A)):
    print("%f" % A[i])


