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