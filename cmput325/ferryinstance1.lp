# testing machine has AMD 3600x, 16 gb 3600mhz cl16 ram

#const steps=13.

car(car1).
car(car2).
car(car3).
car(car4).

location(a).
location(b).
location(c).
location(d).

at(car1,a,0).
at(car2,a,0).
at(car3,c,0).
at(car4,c,0).

at(ferry,a,0).

goal(T):-
at(car1,c,T),
at(car2,b,T),
at(car3,c,T),
at(car4,a,T).