x = 0
for iteration in range(1,101):
	xnew = (2*x**2 +3)/5
	if abs(xnew-x) < 0.000001:
		break
	x = xnew
print('The root : %0.5f' % xnew)
print('The number of iterations : %d' % iteration)