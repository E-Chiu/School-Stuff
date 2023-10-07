A = [1 2 2; 4 4 2; 4 6 4];
b = [3; 6; 10];

[m, n] = size(A);

% apply transformations to turn into U
for i = 1:m
    M = elimMat(A, i);
    A = M*A;
    b = M*b;
end

% check equation can be solved
expX  = [-1; 3; -1];
x = backSubst(A, b);

assert(isequal(expX, x));

% check explicit LU factorization is correct
expL = [1 0 0; 4 1 0; 0 0.5 1];
expU = [1 2 2; 0 -4 -6; 0 0 -1];
A = [1 2 2; 4 4 2; 4 6 4];
[L, U] = myLU(A);

assert(isequal(expL, L));
assert(isequal(expU, U));


