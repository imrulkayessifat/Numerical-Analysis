b = @(x) 2*x^2 - 5*x + 3;
low=input('Enter the value of lower range : '); 
high=input('Enter the value of higher range : ');
tol=input('Enter the  value : ');
if b(low)==0
  fprintf('Lower value is the root\n');
  return
elseif b(high)==0
  fprintf('Higher value is the root\n');
  return
end

if b(high)*b(low)>0
  fprintf('No root exist in that interval\n');
 return 
end


x1=(low+high)/2;
i=1;
fprintf('\n');
while abs(b(x1))>=tol
  x1=(low+high)/2;
  fprintf('  %d\t  %f\t%f\t%f\t%f\n',i,low,high,x1,b(x1));
  i=i+1;
  if b(low)*b(x1)>0
    low=x1;
  else
    high=x1;
  endif
endwhile

