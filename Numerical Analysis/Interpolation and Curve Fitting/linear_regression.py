x = [3,4,5,6,7,8]
y = [0,7,17,26,35,45]
n = len(x)
sumx = sumxy = sumx2 = sumy = 0
for i in range(n):
	sumx += x[i]
	sumy += y[i]
	sumx2 += x[i]**2
	sumxy += x[i]*y[i]
xm = sumx / n
ym = sumy / n

a = (ym*sumx2 - xm*sumxy)/(sumx2 - n*xm**2)
b = (sumxy - xm*sumy)/(sumx2 - n*xm**2)

print('The straight line equation')
print('y = (%.3f) + (%.3f)x' %(a,b))