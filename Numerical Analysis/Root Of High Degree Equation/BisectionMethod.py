y = lambda x: 2*x**2 - 5*x + 3
x1 = float(input('Enter the value x1 : '))
x2 = float(input('Enter the value x2 : '))
y1 = y(x1)
y2 = y(x2)
if y1*y2 > 0:
	print('The root is not within the given interval')
	exit
for bisection in range(1,101):
	xh = (x1 + x2)/2
	yh = y(xh)
	y1 = y(x1)
	if abs(y1) < 1.0E-6:
		break
	elif y1 * yh <0:
		x2 = xh
	else:
		x1 = xh
print('The root : %0.5f' % x1)
print('The number of bisections : %d' % bisection)