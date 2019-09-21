from scipy.optimize import newton,bisect,fsolve,root

f = lambda x: 2*x**2 - 5*x + 3

print(newton(f,0))

print(bisect(f,0,1.2))

print(fsolve(f,0))

print(root(f,0).x)