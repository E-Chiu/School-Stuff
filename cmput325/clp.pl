% solution for question 1

insert_data :-
    assert(c325(fall_2021,aperf,15,15,15,15,75,50)),
    assert(c325(fall_2021,john,14,13,15,10,76,87)),
    assert(c325(fall_2021,lily, 9,12,14,14,76,92)),
    assert(c325(fall_2021,peter,8,13,12,9,56,58)),
    assert(c325(fall_2021,ann,14,15,15,14,76,95)),
    assert(c325(fall_2021,ken,11,12,13,14,54,87)),
    assert(c325(fall_2021,kris,13,10,9,7,60,80)),
    assert(c325(fall_2021,audrey,10,13,15,11,70,80)),
    assert(c325(fall_2021,randy,14,13,11,9,67,76)),
    assert(c325(fall_2021,david,15,15,11,12,66,76)),
    assert(c325(fall_2021,sam,10,13,10,15,65,67)),
    assert(c325(fall_2021,kim,14,13,12,11,68,78)),
    assert(c325(fall_2021,perf,15,15,15,15,80,100)),
    assert(setup(fall_2021,as1,15,0.1)),
    assert(setup(fall_2021,as2,15,0.1)),
    assert(setup(fall_2021,as3,15,0.1)),
    assert(setup(fall_2021,as4,15,0.1)),
    assert(setup(fall_2021,midterm,80,0.2)),
    assert(setup(fall_2021,final,100,0.4)).

% a)

query1(Semester, Name, Total) :-
    c325(Semester, Name, A1G, A2G, A3G, A4G, MG, FG),
    setup(Semester, as1, A1, W1),
    setup(Semester, as2, A2, W2),
    setup(Semester, as3, A3, W3),
    setup(Semester, as4, A4, W4),
    setup(Semester, midterm, Mid, WM),
    setup(Semester, final, Fin, WF),
    Total is (A1G / A1 * W1 +  A2G / A2 * W2 + A3G / A3 * W3 + A4G / A4 * W4 + MG / Mid * WM + FG / Fin * WF) * 100.

% b)
query2(Semester, L) :-
    findall(Name, q2cond(Name, Semester), L).

q2cond(Name, Semester) :-
    c325(Semester, Name, _, _, _, _, MG, FG),
    FG > MG.

% c)
/*
query3(Semester, Name, Type, NewMark) :-
    c325(Semester, Name, A1G, A2G, A3G, A4G, MG, FG),
    retract(c325(Semester, Name, Type, Mark)),
    assert(c325(Name,Type,NewMark)).
*/

/* q2 
example 1:
1) in col 1, row 1, 1,2,3,6,7,8,9 are removed from the domain 
2) in col 2, row 2, 1,3,5,9 are removed from the domain
3) in the middle-most cell of the puzzle 1,2,7,8 are removed from the domain
4) in col 7, row 7, 2,3,5,8,9 are removed from the puzzle
5) in col 9, row 9, 1,3,5,8,9 are removed from the puzzle

example 2:
4 cannot be removed from the domain since it does not show up anywhere else
*/

% q3

:- use_module(library(clpfd)).

encrypt(W1,W2,W3) :- 

    length(W1,N),           % if you need to know the lengths of words
 
    length(W3,N1),   
 
    append(W1,W2,W),
 
    append(W,W3,L),
 
    list_to_set(L,Letters),     % remove duplicates, a predicate in the list library
 
    [LeadLetter1|_] = W1,   % identify the leading letter to be set to non-zero
 
    [LeadLetter2|_] = W2,
 
    [LeadLetter3|_] = W3,
 
    !,                      % never need to redo the above
 
    Letters ins 0..9, 
    all_different(Letters),

% q4

/* 
The goal of Sudoku is to fill in a 9 by 9 grid with digits 
so that each column, row, and 3 by 3 section contain the 
numbers between 1 to 9. At the beginning of the game, 
the 9 by 9 grid will have some of the squares filled in. 
Your job is to fill in the missing digits and complete the grid. 

*/

:- use_module(library(clpfd)).


sudoku(Rows) :-
    grid(9, Rows),
        % Rows now is a 9x9 grid of variables
    append(Rows, Vs),
        % Vs is a list of all 9*9 variables in Rows
    Vs ins 1..9,
    xall-distinct(Rows),
        % Variables of each row get distinct values
    xtranspose(Rows, Columns),
        % get the columns of 9x9 grid
    xall-distinct(Columns),
    Rows = [As,Bs,Cs,Ds,Es,Fs,Gs,Hs,Is],
        % need references to rows
    blocks(As, Bs, Cs),
        % deal with three rows at a time
    blocks(Ds, Es, Fs),
    blocks(Gs, Hs, Is).

blocks([], [], []).
blocks([N1,N2,N3|Ns1], [N4,N5,N6|Ns2], [N7,N8,N9|Ns3]) :-
    all_distinct([N1,N2,N3,N4,N5,N6,N7,N8,N9]),
    blocks(Ns1, Ns2, Ns3).

problem(P) :-
    P = [[1,_,_,8,_,4,_,_,_],
	 [_,2,_,_,_,_,4,5,6],
	 [_,_,3,2,_,5,_,_,_],
	 [_,_,_,4,_,_,8,_,5],
	 [7,8,9,_,5,_,_,_,_],
	 [_,_,_,_,_,6,2,_,3],
	 [8,_,1,_,_,_,7,_,_],
	 [_,_,_,1,2,3,_,8,_],
	 [2,_,5,_,_,_,_,_,9]].

t(Rows) :-
    problem(Rows),
    sudoku(Rows),
    maplist(labeling([ff]), Rows),
    maplist(writeln, Rows).

/* - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
   Example:
   ?- t(Rows).
   [1,5,6,8,9,4,3,2,7]
   [9,2,8,7,3,1,4,5,6]
   [4,7,3,2,6,5,9,1,8]
   [3,6,2,4,1,7,8,9,5]
   [7,8,9,3,5,2,6,4,1]
   [5,1,4,9,8,6,2,7,3]
   [8,3,1,5,4,9,7,6,2]
   [6,9,7,1,2,3,5,8,4]
   [2,4,5,6,7,8,1,3,9]
   Rows = [[1, 5, 6, 8, 9, 4, 3, 2|...], [9, 2, 8, 7, 3, 1, 4|...], [4, 7, 3, 2, 6, 5|...], [3, 6, 2, 4, 1|...], [7, 8, 9, 3|...], [5, 1, 4|...], [8, 3|...], [6|...], [...|...]].

*/

xtranspose([], []).
xtranspose(R, C) :-
    