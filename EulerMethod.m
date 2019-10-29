eu = @(x,y) x+y;
x0=input('Enter intial value of x : ');
y0=input('Enter intial value of y or eu(x)=y : ');
h=input('Enter the value of increamentor : ');
xn=input('Enter the last value of x for showing eu(xn)=yn : ');
i=1;
fprintf('\n');
while x0<=xn
  y0=y0+h*eu(x0,y0);
  fprintf('   %d\t  %f\t%f\n',i,x0,y0);
  x0=x0+h;
  i=i+1;
endwhile
