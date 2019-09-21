x = [0.0,1.5,2.8,4.4,6.1,8.0]
y = [0.0,0.9,2.5,6.6,7.7,8.0]
n = len(x) -1
import numpy as np
Dy = np.zeros((n+1,n+1))
Dy[:,0] = y
for j in range(n):
	for i in range(j+1,n+1):
		Dy[i,j+1] = (Dy[i,j] - Dy[j,j])/(x[i] - x[j])
print(Dy)

xp = float(input('Enter x : '))
yp = Dy[0,0]
for i in range(n):
	xprod = 1
	for j in range(i+1):
		xprod *= xp - x[j]
	yp += xprod * Dy[i+1,i+1]
print('For x = %.1f, y = %.1f' % (xp,yp))