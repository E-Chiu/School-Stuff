function [eigenVal, eigenVec] = powerIteration(A)
    % create initial vector
    x = [0 1].';
    % do power iteration 1000 times to try and converge to values
    for k = 1:1000
        yk = A*x;
        yNorm = norm(yk,Inf);
        x = yk/yNorm;
    end
    % get eigenVec
    eigenVec = ceil(x);
    % do Rayleigh quotient to get eigenVal
    eigenVal = (eigenVec.'*A*eigenVec)/(eigenVec.'*eigenVec);
end