import numpy as np

'''
A=np.random.randint(0,10,[2,3])
print('Matrix A')
print(A)
'''
# which is used to change a 2-dimensional array or a multi-dimensional array into a contiguous flattened array
A=np.random.randint(0,10,[2,3])
print('Matrix A')
print(A)
print('Ravel A')
print(np.ravel (A))

'''
# Sum
#print (A.sum())

# Sum on axis 0 = vertical
print ('vertical sum')
print (A.sum(axis=0))

# Sum on axis 0 = vertical
print ('horizontal sum')
print (A.sum(axis=1))

# Sum cummulated
print ('cummulated sum')
print (A.cumsum())

#min on axis 0 vertical
print ('min on axis=0 -> vertical ')
print (A.min (axis=0))

#Position of min on axis 1 horizotal
print ('Position of min on axis=1-> horizotal ')
print (A.argmin (axis=1))

#Exponential
print("exponatial of A")
print(np.exp(A))

#startistics

#mean
print("the mean")
print(A.mean())

#variance
print("variance ")
print(A.var())

#ecart type
print("Ecart type ")
print(A.std())

#corr coef
print("Coeffiecient of correllation ")
print(np.corrcoef(A))
print("Coeffiecient of correllation  1line and 2 col")
print(np.corrcoef(A)[0,1])

'''

# number of repetition in a matrix
'''
print(A)
print("print the number of repetition of each element of the matrice")
print(np.unique(A,return_counts=True))
'''
# sort the number of occurance  of  number in a dataset
'''
values, counts = np.unique(A,return_counts=True)
values[counts.argsort()]
print("The number of occurences")
print(counts)
print("The sorted value of occurences")
print(values )
'''

# Linear algebra
'''
A= np.ones((2,3))
B = np.ones((3, 2))

print (A)
print (B)
'''
#Transpose
'''
print (" transposé ")
print (A.T)
print (B.T)
'''
#Matriciel Product
'''
print( "A*B =")
print(A.dot(B))
print("B*A =")
print(B.dot(A))

'''
#matrice inversion
'''
A=np.random.randint(0,10,[3,3])

print('det of A')
print (np.linalg.det(A))

print('invert of A')
print (np.linalg.inv(A))

# proper eigen  value and vector
print('proper value or eigun value  and vector of A')
print (np.linalg.eig(A))
'''
#Broadcasting ( only column
'''
A=np.random.randint(1,10, [4,3])
B=np.ones([4,3])
print("Matrice A:")
print(A)
print("Matrice B:")
print (B)
print("Matrice A+B:")
print (A+B)
'''

#standardize a matrix  (A- mean (A))/ sigma A
'''
np.random.seed(0)  # the same set of numbers will appear every time.
A = np.random.randint(0,100,[10, 5])
print(A)
print ("A standardized")
D= (A - A.mean(axis=0))/A.std(axis=0)
print(" Matrix standardized D")
print (D)

print ('the mean of D')
print(D.mean(axis=0))
print ('the standard deviation of D')
print(D.std(axis=0))

'''


























