x = 5
xnew = 0
iteration = 0
while abs(xnew - x) >= 0.000001:
	iteration +=1
	x = xnew
	xnew = (2*x**2 +3)/5
print('The root : %0.5f' % xnew)
print('The number of iterations : %d' % iteration)