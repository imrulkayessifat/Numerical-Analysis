f = @(x) 2*x^2 - 5*x + 3;
low=input('Enter the value of lower range : '); 
high=input('Enter the value of higher range : ');
tol=input('Enter the tolerence value : ');

if f(low)==0
  fprintf('Lower value is the root\n');
  return
elseif f(high)==0
  fprintf('Higher value is the root\n');
  return
end

if f(high)*f(low)>0
  fprintf('No root exist in that interval\n');
 return 
end

x1=(low*f(high)-(high*f(low)))/(f(high)-f(low));
i=1;
fprintf('\n');
while abs(f(x1))>=tol
  x1=(low*f(high)-(high*f(low)))/(f(high)-f(low));
  fprintf('  %d\t  %f\t%f\t%f\t%f\n',i,low,high,x1,f(x1));
  i=i+1;
  if f(low)*f(x1)>0
    low=x1;
  else
    high=x1;
  endif
endwhile