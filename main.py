from finite_automata.finite_automata import FiniteAutomata as FA

# Create a finite automata
fa = FA(states=5,
        alphabet=['a', 'b'],
        trans=[(0, 'a', 1), (0, 'a', 2), (0, 'b', 2), (1, 'a', 3),
               (2, 'b', 3), (3, 'a', 4), (3, 'b', 0), (3, 'b', 5)],
        init_state=0,
        accepting=[4])

# Display the finite automata graphically
fa.display()
print(fa.evaluate('aabbbbaba', detailed=True))
