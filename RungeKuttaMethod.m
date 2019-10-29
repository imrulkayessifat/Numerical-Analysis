f = @(x,y) x*y;
x0=input('Enter initial value of x : ');
y0=input('Enter initial value of y : ');
h=input('Enter interval gap h : ');
xn=input('Enter final value of x : ');
i=1;
fprintf('\n');
while x0<=xn
  k1=h*f(x0,y0);
  k2=h*f((x0+(h/2)),(y0+(k1/2)));
  k3=h*f((x0+(h/2)),(y0+(k2/2)));
  k4=h*f((x0+h),(y0+k3));
  delY=(k1+2*k2+2*k3+k4)/6;
  y0=y0+delY;
  x0=x0+h;
  fprintf('%d\t%f\t%f\n',i,x0,y0);
  i=i+1;
endwhile
