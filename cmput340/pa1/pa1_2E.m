A = [1 2 3; 3 2 4; 1 3 2];
b = [1; 1; 3];

% apply transformations to turn into U
[L, U] = myLU(A);

x = fwdSubst(L, b);

% check answer is correctly solved
x = backSubst(U, x);