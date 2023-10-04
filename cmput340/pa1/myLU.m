function [L, U] = myLU(A)
    dim = size(A, 1);
    
    % get the intial elementary elimination matrices
    [M, L] = elimMat(A, 1);
    % apply elimination Matrix
    Aprime = M*A;
    % loop through the columns
    for k = 2:dim-1
        % compute elim matrices
        [mk, mkInv] = elimMat(Aprime, k);
        % multiply inverse to L
        L = L*mkInv;
        % multiple normal to M
        M = M*mk;
        % apply elimination to Aprime
        Aprime = mk*Aprime;
    end
    % get U
    U = Aprime;