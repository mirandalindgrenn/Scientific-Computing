import numpy as np

def g_fun(x):
   return x**2*np.sin(x)

a,b = 1, 3  
result = np.empty(N)
for k in range(N):
   u = np.random.uniform(a, b)
   result[k] = g_fun(u)
int_mc = (b-a)*np.mean(result)

print(abs(5.55342325-int_mc))  


def BrownMotion(initial_pos, end_time, time_step):
   x=initial_pos
   n, m=initial_pos.shape
   k=0
   while k*time_step<=end_time:
      chance=stock(np.array, end_time)
      new_pos=x[:-1] + chance
      x=np.column_stack((x, new_pos))
      k+=1
   return x


for k in range(1, 11):
   n=