import numpy as np
import math
sigma=np.array([[3, 0, 0], [0, math.sqrt(5), 0], [0, 0, 2]])
Ut=np.array([[0, 0, -1, 0,0],[-1/math.sqrt(5), 0, 0,0, -2/math.sqrt(5)], [0, -1, 0,0,0]])
V=np.array([[0, -1, 0], [-1, 0, 0], [0,0, 0], [0,0, -1]])
sigma_inv=np.linalg.inv(sigma)
pseudo=V@sigma_inv@Ut
b=np.array([[1],[4], [3],[0],[2]])

x_=pseudo@b
x=b


#sigma2=np.array([[3, 0, 0, 0], [0, math.sqrt(5), 0, 0], [0, 0, 2, 0], [0,0,0,0], [0,0,0,0]])
#U=np.array([[0,-1/math.sqrt(5), 0,0,-2/math.sqrt(5)], [0,0,-1,0,0], [0,0,0,1,0], [0,-2/math.sqrt(5), 0,0,1/math.sqrt(5)]])
#V2=np.array([[0, -1, 0, 0], [-1, 0, 0, 0], [0,0, 0, -1], [0,0, -1, 0]])
#A=U@sigma2@V2
#At=A.T
#AtA=At@A
#atainv=np.linalg.inv(AtA)
#x=atainv@At@b



print(f"matrisen för pseudo är {pseudo}")
print('\n')
print(f"pseudo*b=x resulterar i x= \n {x_}")







