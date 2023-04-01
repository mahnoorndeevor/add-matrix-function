import numpy as np
def addmat():
   A=[]
   B=[]
   n=int(input("Enter A no of row: "))
   p=int(input("Enter B no of col: "))
   g=int(input("Enter A no of row: "))
   s=int(input("Enter B no of col: "))


   for i in range(0, n):
     a=[]
     for j in range(0, p):
       ele1=int(input("input A: "))
       a.append(ele1)
     A.append(a)
     print(A)

   for i in range(0, g):
     b=[]
     for j in range(0, s):
       ele2=int(input("input B: "))
       b.append(ele2)
     B.append(b)
    
     print(B)
   
    
    
   if np.size(A)==np.size(B):
    
      C =np.array(A)+np.array(B)
      print(C)
   else:
      print("not possible")
 
   return C

MatrixC=addmat()
print("MatrixC: ", str(MatrixC))
print("Ans: ", str(MatrixC/2))