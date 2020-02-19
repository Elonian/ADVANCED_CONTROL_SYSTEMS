import numpy as np
import itertools as itert
import math
import matplotlib.pyplot as plt
import control
import scipy as sp

degree=int(input("Degree of the polynomial:"))          #enter degree


if degree %2 == 1 :
   c=np.zeros(degree+3)
else :
   c =np.zeros(degree+4)                                    # creatating a array of zeros 
print("Enter the coefficients" )  # coefficients in order 
for i in range(0,degree+1):                                
	c[i]=input("")                   #taking coefficients as input

Rou_matrix=np.zeros([degree+1,degree+1])            #forming first and second row in the routh matrix
for j in range (0,degree-1):
	Rou_matrix[0,j]=c[2*j]
	Rou_matrix[1,j]=c[(2*j)+1]
	
	
	
for i in range(2,degree+1):                                   #calculating the remaining rows in yhe routh matrix
	for j in range (0,degree-1):
		Rou_matrix[i,j]= (((Rou_matrix[i-1,0]*Rou_matrix[i-2,j+1])-(Rou_matrix[i-1,j+1]*Rou_matrix[i-2,0]))/(Rou_matrix[i-1,0]))
	if(Rou_matrix[i,0]== 0):
		
		Rou_matrix[i,0]=0.00001
			
rou_first_row=[]
for i in range (0,degree+1):             #taking the first row elements 
	rou_first_row.append(Rou_matrix[i,0])

sign_changes=(len(list(itert.groupby(rou_first_row, lambda rou_first_row: rou_first_row > 0)))-1)     #calculating no of sign changes 
if sign_changes==0:
	print("No poles on right half of s plane")
else:
	print("No.of poles on right half of s plane is:",sign_changes) 
print(Rou_matrix)
