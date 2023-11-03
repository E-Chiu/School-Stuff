function [eigenVals, eigenVecs] = qrIteration(A)
    % do power iteration 1000 times to try and converge to values
    eigenVecs = eye(size(A,1));
    for k = 1:1000
        % get qr factorization
        [Q, R] = qr(A);
        A = R*Q;
        % multiply Q to previous Q to get eigenvalues
        eigenVecs = eigenVecs * Q;
    end
    % get eigenVals from diagonal
    eigenVals = diag(A);
end