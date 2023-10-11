function x = backSubst(U, y, k)
% Backwards substitution
[m,n]=size(U);
if ~exist('k') % If first call won't have k
    k=n;
end

x=y(k)/U(k,k);
if k > 1 % recursive step
    u = [U(1:k,k);zeros(abs(k-m),1)];
    x = [x;backSubst(U,y-x*u,k-1)];
end