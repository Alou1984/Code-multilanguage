import numpy as np

A= np.array([[1,2,3],[4,5,6],[7,8,9]])
'''
B=A[0:2,0:2]
print(B.shape)
A[0:2,0:2]=100
C=A[:,-2]
D= A[:,-2:]
print (A)
print(A.shape)
print (B)
print(B.shape)
print (C)
print(C.shape)
print (D)
print(D.shape)
'''
# Zeros and slicing
'''
E= np.zeros((4,4))
print (E)
print(E.shape)
E[1:3,1:4]= 77
print (E)
'''
# Zeros and slicing by step
'''
E1= np.zeros((9,9))
print (E1)
print(E1.shape)
E1[::2,::2]= 1
print (E1)
'''
# boolean indexing
F=np.random.randint(1,10,[6,6])
print(F)
print (F<6)
G=F
G[G<6]=100
print(G)










