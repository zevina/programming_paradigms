sum([],0).
sum([N|T],Sum) :-
    sum(T,Sum1), Sum is Sum1 + N.