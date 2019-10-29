f = @(x) 2*x^2 - 5*x + 3;
fp = @(x) 4*x - 5;
x1=input('Enter the intial guess : ');
tol=input('Enter the tolerence value : ');
if f(x1)==0
  fprintf('Lower value is the root\n');
  return
end

i=1;
fprintf('\n');
while abs(f(x1))>=tol
  x2=x1-(f(x1)/fp(x1));
  fprintf('  %d\t  %f\t%f\n',i,x2,f(x2));
  i=i+1;
  x1=x2;
endwhile