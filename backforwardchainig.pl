parent(john, sarah).
parent(sarah, emma).
parent(sarah, mike).
parent(john, peter).


ancestor(X, Y) :- parent(X, Y).
ancestor(X, Y) :- parent(X, Z), ancestor(Z, Y).
