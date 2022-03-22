% q1: the setDifference predicate takes 2 lists S1, S2 and returns the difference of the two lists in S3
% the code for the member predicate is taken from class slides
member(E, [E | _]).
member(E, [_ | L]) :- member(E, L).

setDifference([], _, []).
setDifference([A], [A], []).
setDifference([A], [_], [A]).
setDifference([A], [], [A]).
setDifference([], [_], []).
setDifference([A|S1], S2, S3) :- % ignore if is a member
    member(A, S2),
    setDifference(S1, S2, S3).
setDifference([A|S1], S2, [A|S3]) :-
    setDifference(S1, S2, S3).


% q2: the swap predicate takes a list and every pair of elements in the list are swapped
swap([], []).
swap([A], [A]).
swap([A, B|L], [B, A| R]) :- 
    swap(L, R).

% q3: the filter predicate takes a possibly nested list of numbers and returns a list of numbers that satisfy specifications
% the flatten predicate is taken from the classs slides
flatten([],[]).
flatten([A|L],[A|L1]) :-
 xatom(A), flatten(L,L1).
flatten([A|L],R) :-
 flatten(A,A1), flatten(L,L1), append(A1,L1,R).

xatom(A) :- atom(A).
xatom(A) :- number(A).

filter(L,OP,N,L1) :-
    flatten(L, A),
    filterHelper(A, OP, N, L1).

filterHelper([], _, _, []). % general base case
filterHelper([A|L], greaterThan, N, [A|L1]) :- % when is greater than
    A > N,
    filterHelper(L, greaterThan, N, L1).
filterHelper([A|L], greaterThan, N, L1) :- % go to next when isn't greater than
    A =< N,
    filterHelper(L, greaterThan, N, L1).
filterHelper([A|L], equal, N, [A|L1]) :- % when is equal
    A == N,
    filterHelper(L, equal, N, L1).
filterHelper([A|L], equal, N, L1) :- % go to next when isn't equal
    A =\= N,
    filterHelper(L, equal, N, L1).
filterHelper([A|L], lessThan, N, [A|L1]) :- % when is less than
    A < N,
    filterHelper(L, lessThan, N, L1).
filterHelper([A|L], lessThan, N, L1) :- % go to next when isn't greater than
    A >= N,
    filterHelper(L, lessThan, N, L1).

% q4: the countAll predicate counts the occurance of every atom in the list and sorts them
% modMember is a modified member from the class slides that checks within nested lists
countAll(L, N) :-
    countAllHelper(L, [], N).

countAllHelper([], _, _).
countAllHelper([A | L], [], L1) :- % if not found add to list
    countAllHelper(L, [[A, 1] | L1], [[A, 1] | L1]).
countAllHelper([A | L], [[B | [C | _]] | L1], [[B , C1] | L2]) :- % if found then increment
    A = B,
    C1 is C + 1,
    countAllHelper(L,  [[B , C1] | L2], L2). % update list
countAllHelper([A | L], [_ | L1], L2) :- % if not found check next
    countAllHelper([A | L], L1, L2).

% q5: the sub predicate takes a list of pairs [xi, ei] and searches through a list, replacing every occurance of xi with ei in the list
% NOTE I WAS UNABLE TO REPRODUCE THE NESTED STRUCTURE WHEN I SUBSTITUTE, BUT FLATTEN WAS NOT USED, I ENTERED THE NESTED
% LISTS PROPERLY.
sub([], _, []).
sub([A | L], S, [B | L1]) :- % if atom check if need to be replaced
    atom(A),
    sub(L, S, L1),
    subHelper(A, S, B).
sub([A | L], S, L1) :- % if nested search both parts
    \+ atom(A),
    sub(A, S, L2),
    sub(L, S, L3),
    append(L2, L3, L1).

subHelper(A, [], A). % if sub list empty add to list and go back
subHelper(A, [[B | [C | _]] | _], C) :- % if found in sub list substitute
    A = B.
subHelper(A, [[B | _] | S], C) :- % otherwise keep searching list
    \+ A = B,
    subHelper(A, S, C).

% q6: the clique predicate 
% clique(L).

% q7: