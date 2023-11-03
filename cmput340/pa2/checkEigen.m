A = [1 2 3; 2 3 1; 3 1 2];
[eigenVecs, eigenVals] = eigs(A);
eigenVals = diag(eigenVals);

% check for power iteration
[powerVal, powerVec] = powerIteration(A);
ism = ismembertol(powerVal, eigenVals);
assert(ism);
% see if Ax = lambdaX for any of the eigenVals matlab finds
Ax = A*powerVec;
lambdaX = [];
for i = 1:size(eigenVals,1)
    lambdaX = [lambdaX eigenVals(i)*powerVec];
end
ism = ismembertol(Ax, lambdaX);
assert(all(ism));

% check for inverse iteration
[inverseVal, inverseVec] = inverseIteration(A);
ism = ismembertol(inverseVal, eigenVals);
%assert(ism);
% see if Ax = lambdaX for any of the eigenVals matlab finds
Ax = A*inverseVec;
lambdaX = [];
for i = 1:size(eigenVals,1)
    lambdaX = [lambdaX eigenVals(i)*inverseVec];
end
%assert(ismembertol(inverseVec, eigenVecs));

% check for qrIteration
[qrVals, qrVecs] = qrIteration(A);
for val = 1:size(qrVals, 1)
    assert(ismembertol(qrVals(val), eigenVals));
end
for vec = 1:size (qrVecs, 2)
    Ax = A*qrVecs(vec);
    for i = 1:size(eigenVals,1)
        lambdaX = [lambdaX eigenVals(i)*qrVecs(vec)];
    end
    ism = ismembertol(Ax, lambdaX);
end