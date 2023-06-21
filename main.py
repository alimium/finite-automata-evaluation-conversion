from finite_automata import FiniteAutomata as FA


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
    init_state = input('Enter Initial State Number (0 by Default): ')
    for i in range(int(acc_size)):
        accepting.append(int(input(f'Enter Accepting state {i+1}: ')))
    for i in range(int(trans_size)):
        p, s, q = input(f'Enter Transition Rule {i+1}: ').split(' ')
        trans.append((int(p), s, int(q)))
    for i in range(int(str_size)):
        test_strings.append(input(f'Enter Test String {i}: '))

    return states, alphabet, trans, init_state, accepting, test_strings


# states, alphabet, trans, init_state, accepting, test_strings = parse_input()

states = 5
alphabet = ['a', 'b']
trans = [(0, 'a', 1), (1, 'a', 0), (0, 'b', 4), (0, 'a', 2),
         (2, 'a', 3), (3, 'b', 0)]
init_state = 0
accepting = [4]
test_strings = ['aaa', 'aab']

# Create a finite automata
fa = FA(states=states,
        alphabet=alphabet,
        trans=trans,
        init_state=init_state,
        accepting=accepting)

# Display the finite automata graphically
fa.display()
for string in test_strings:
    print(fa.evaluate(string))

# 5 2 1 6 2
# a
# b
# 0
# 4
# 0 a 1
# 1 a 0
# 0 b 4
# 0 a 2
# 2 a 3
# 3 b 0
# aaa
# aab
