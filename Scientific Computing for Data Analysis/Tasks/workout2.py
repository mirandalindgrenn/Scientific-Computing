import numpy as np

#löser matrismultiplikation
A=np.array([[1,9], [1, 10], [1,11], [1, 12], [1,13]])
AT=np.array([[9, 10, 11, 12, 13], [1, 1, 1, 1, 1]])
y=np.array([5, 5, 4, 3, 1])
a=np.array([14.6, -1])
e=y-np.dot(A,a) #dot beräknar matrismultiplikation mellan A och a
mean=np.array([[1, 11], [1, 11], [1, 11], [1, 11],[1, 11]])
meanT=np.array([[11, 11, 11, 11, 11], [1, 1, 1, 1, 1]])
A_AT=np.dot(AT, A)
print(A_AT)

print(f" till A*AT {np.linalg.cond(A_AT)}")
print(f"Löser ekvationen i 2.1 till matrisen {np.linalg.solve(AT@A, AT@y)}") #löser en matrisekvation
print(f"Beräknar matrisen till i uppgift 2.2: {e}")
#print(f"Löser ekvationen i 2.1 till matrisen {np.linalg.solve(meanT@mean, meanT@y)}")



