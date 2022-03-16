% q1: the setDifference function takes 2 lists S1, S2 and returns the difference of the two lists in S3
% the code for the member function is taken from class slides
member(E, [E | _]).
member(E, [_ | L]) :- member(E, L).

setDifference([], _, []).
setDifference([A], [A], []).
setDifference([A], [B], [A]).
setDifference([A], [], [A]).
setDifference([], [B], []).
setDifference([A|S1], S2, S3) :-
    member(A, S2),
    setDifference(S1, S2, S3).
setDifference([A|S1], S2, [A|S3]) :-
    setDifference(S1, S2, S3).


% q2: the swap function takes a list and every pair of elements in the list are swapped
swap([], []).
swap([A], [A]).
swap([A, B|L], [B, A| R]) :- 
    swap(L, R).

% q3: the filter function takes a possibly nested list of numbers and returns a list of numbers that satisfy specifications
% the flatten function is taken from the classs slides
flatten([],[]).
flatten([A|L],[A|L1]) :-
 xatom(A), flatten(L,L1).
flatten([A|L],R) :-
 flatten(A,A1), flatten(L,L1), append(A1,L1,R).

xatom(A) :- atom(A).
xatom(A) :- number(A).

filter(L,OP,N,L1) :-
    flatten(L, A).
    filterHelper(A, OP, N, L1).

filterHelper([A|L], greaterThan, N, L1).

filterHelper(L, equal, N, L1).

filterHelper(L, lessThan, N, L1).

% q4: the countAll function counts the occurance of every atom in the list
countAll(L,N).

% q5: the sub function takes a list of pairs [xi, ei] and searches through a list, replacing every occurance of xi with ei in the list
sub(L, S, L1).