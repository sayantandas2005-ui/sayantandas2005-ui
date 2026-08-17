% Small MATLAB numerical-computing demonstration
% Solves a simple nonlinear equation with Newton's method.

f = @(x) x.^2 - 2;
df = @(x) 2*x;
x = 1.0;

for k = 1:10
    x = x - f(x) / df(x);
end

fprintf('Approximate sqrt(2): %.8f\n', x);
