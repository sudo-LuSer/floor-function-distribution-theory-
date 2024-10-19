import matplotlib.pyplot as plt 
import numpy as np
def u(t):
	if(t>0):
		return 1
	return 0 
n = 1000
def E(t):
	if(t<0):
		return -E(-t) -1
	res = 0 
	i = 0
	while(i<=n):
		res += i*(u(t-i) - u(t-i-1))
		i+=1 
	return res 
X = np.arange(-10, 10 , 0.01)
Y = []
for i in X:
	Y.append(E(i))
plt.plot(X , Y)
plt.show()