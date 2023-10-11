A = [1 2 2; 4 4 2; 4 6 4];
b = [3; 6; 10];

[m, n] = size(A);

% apply transformations to turn into U
for i = 1:m
    M = elimMat(A, i);
    A = M*A;
    b = M*b;
end

% check answer is correctly solved
expX  = [-1; 3; -1];
x = backSubst(A, b);

assert(isequal(expX, x));
