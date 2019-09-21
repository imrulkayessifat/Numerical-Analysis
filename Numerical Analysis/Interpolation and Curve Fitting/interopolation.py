y = lambda xp,x1,x2,y1,y2: y1 + (y2-y1)/(x2-x1)*(xp-x1)
x = y(50,40,60,61.6,71.2)
print("The temparature is %f" % x)