from numpy import array,sum,mean

x = array([3,4,5,6,7,8],float)
y = array([0,7,17,26,35,45],float)
n = len(x)

a = (mean(y)*sum(x**2) - mean(x)*sum(x*y))/(sum(x**2)-n*mean(x)**2)
b = (sum(x*y) - mean(x)*sum(y))/(sum(x**2)-n*mean(x)**2)

print('The straight line equation')
print('y = (%.3f) + (%.3f)x' %(a,b))