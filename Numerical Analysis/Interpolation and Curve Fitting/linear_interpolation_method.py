time = [0,20,40,60,80,100]
temp = [26.0,48.6,61.6,71.2,74.8,75.2]

def y(xp,x,y):
	for i,xi in enumerate(x):
		if xp < xi:
			return y[i-1]+(y[i]-y[i-1])/(x[i]-x[i-1])*(xp-x[i-1])
	else:
		print('Given x-value is out of range')

temp50 = y(50,time,temp)
print('The temperature = %f' % temp50)