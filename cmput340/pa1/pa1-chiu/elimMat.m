function [M_k, L_k] = elimMat(A, k)
    dim = size(A, 1);
    % get the column we want to eliminate
    kCol = A(:, k);
    %get the pivot
    pivot = kCol(k);
    % create vector of 0s for m
    m = zeros(k, 1);
    % get mk+1 onwards
    mkp1 = kCol(k+1:end);
    % divide by pivot
    mkp1 = mkp1/pivot;
    %combine to get the whole column
    m = [m; mkp1];
    % create an identity matrix
    ident = eye(dim);
    % ek is the kth column of I
    ek = ident(:, k);
    % get the elementary elimination matrix
    M_k = ident - m * ek.';
    L_k = ident + m * ek.';
