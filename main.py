from finite_automata import FiniteAutomata as FA
from finite_automata.enfa import EpsilonNonDeterministicFiniteAutomata as ENFA


def parse_input() -> None:
    q_size, alph_size, acc_size, trans_size, str_size = input(
        'Enter Configurations (q,s,a,m,n): ').split(' ')

    states = int(q_size)
    alphabet = []
    trans = []
    init_state = 0
    accepting = []
    test_strings = []

    for i in range(int(alph_size)):
        alphabet.append(input(f'Enter alphabet {i+1}: '))
    init_state = int(input('Enter Initial State Number (0 by Default): '))
    for i in range(int(acc_size)):
        accepting.append(int(input(f'Enter Accepting state {i+1}: ')))
    for i in range(int(trans_size)):
        p, s, q = input(f'Enter Transition Rule {i+1}: ').split(' ')
        trans.append((int(p), s, int(q)))
    for i in range(int(str_size)):
        test_strings.append(input(f'Enter Test String {i+1}: '))

    return states, alphabet, trans, init_state, accepting, test_strings


# Default input
states = 7
alphabet = ['a', 'b']
trans = [(0, 'a', 0), (0, '$', 1), (0, '$', 4), (1, 'a', 2), (2, 'b', 3),
         (3, 'b', 1), (4, 'b', 4), (4, '$', 5), (5, 'b', 6), (6, 'a', 5)]
init_state = 0
accepting = [1, 5]
test_strings = ['$', 'aaa', 'aaab', 'abb', 'abbab', 'abbaba', 'abbc']


# UNCOMMENT NEXT LINE TO USE CUSTOM INPUT
# states, alphabet, trans, init_state, accepting, test_strings = parse_input()

# Create a finite automata
fa = ENFA(states=states,
          alphabet=alphabet,
          trans=trans,
          init_state=init_state,
          accepting=accepting)

# Display the finite automata graphically
fa.display()
print(fa)

# Evaluate strings
for string in test_strings:
    print(fa.evaluate(string))
# fa.to_DFA() # NOT WORKING PROPERLY YET

# 7 2 2 10 7
# a
# b
# 0
# 1
# 5
# 0 a 0
# 0 $ 1
# 0 $ 4
# 1 a 2
# 2 b 3
# 3 b 1
# 4 b 4
# 4 $ 5
# 5 b 6
# 6 a 5
# $
# aaa
# aaab
# abb
# abbab
# abbaba
# abbc
