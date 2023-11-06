A = [2 0 3; 0 3 0; 0 0 3]; % random diagonalizable matrix i found
[eigenVecs, eigenVals] = eigs(A);
eigenVals = diag(eigenVals);

% check for power iteration
[powerVal, powerVec] = powerIteration(A);
ism = ismembertol(powerVal,max(eigenVals));
assert(ism);
% see if Ax = lambdaX
Ax = A*powerVec;
lambdaX = max(eigenVals)*powerVec;
ism = ismembertol(Ax,lambdaX);
assert(all(ism));

% check for inverse iteration
[inverseVal, inverseVec] = inverseIteration(A);
ism = ismembertol(inverseVal,min(eigenVals));
assert(ism);
% see if Ax = lambdaX
Ax = A*inverseVec;
lambdaX = min(eigenVals)*inverseVec;
ism = ismembertol(Ax,lambdaX);
assert(all(ism));

% check for qrIteration
[qrVals, qrVecs] = qrIteration(A);
for val = 1:size(qrVals, 1)
    assert(ismembertol(qrVals(val), eigenVals));
end
for vec = 1:size(qrVecs, 2)
    found = 0;
    Ax = A*qrVecs(:,vec);
    for i = 1:size(eigenVals,1)
        lambdaX = eigenVals(i)*qrVecs(:,vec);
        ism = ismembertol(Ax, lambdaX);
        if all(ism)
            found = 1;
        end
    end
    if ~found
        error("eigenvec not found")
    end
end