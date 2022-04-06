#const steps=20.

car(car1).
car(car2).
car(car3).
car(car4).
car(car5).

location(a).
location(b).
location(c).
location(d).
location(e).

at(car1,a,0).
at(car2,a,0).
at(car3,b,0).
at(car4,c,0).
at(car5,e,0).

at(ferry,a,0).

goal(T):-
at(car1,e,T),
at(car2,d,T),
at(car3,c,T),
at(car4,b,T),
at(car5,a,T).