% q1: the setDifference function takes 2 lists S1, S2 and returns the difference of the two lists in S3
% setDifference(+S1, +S2, -S3).

member(E, [E | _]).
member(E, [_ | L]) :- member(E, L).

% q2: 

swap(L, R).
swap([_|L], [L|_]).
