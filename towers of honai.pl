% Move a single disk from one peg to another.
move(1, Source, Target, _) :-
    write('Move disk 1 from '),
    write(Source),
    write(' to '),
    write(Target),
    nl.

% Move N disks from Source peg to Target peg using the Auxiliary peg.
move(N, Source, Target, Auxiliary) :-
    N > 1,
    M is N - 1,
    move(M, Source, Auxiliary, Target),
    move(1, Source, Target, _),
    move(M, Auxiliary, Target, Source).

% Predicate to solve the Towers of Hanoi puzzle with N disks.
towers_of_hanoi(N) :-
    move(N, 'A', 'C', 'B').

% Example usage:
% ?- towers_of_hanoi(3).
