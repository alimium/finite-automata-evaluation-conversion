from queue import LifoQueue
from finite_automata.finite_automata import FiniteAutomata
from finite_automata.dfa import DefiniteFiniteAutomata


class EpsilonNonDeterministicFiniteAutomata(FiniteAutomata):
    def __init__(self, states=None, alphabet=None, init_state=None, accepting=None, trans=None) -> None:
        super().__init__(states, alphabet, init_state, accepting, trans)

# TODO: Complete this method ===========================================
    # def to_DFA(self) -> DefiniteFiniteAutomata:
    #     # TODO: convert enfa to dfa
    #     new_trans = {}
    #     for c in self.alphabet:
    #         for q in self.states:
    #             visited_alphabet = False
    #             stack = LifoQueue()
    #             new_alphabet_trans = set()
    #             if (q, c) in self.trans.keys():
    #                 stack.put((q, c))
    #             if (q, '.') in self.trans.keys():
    #                 stack.put((q, '.'))
    #             while stack.qsize() > 0:
    #                 curr_state, curr_char = stack.get()
    #                 next_states = self.trans[(curr_state, curr_char)]

    #                 for state in next_states:
    #                     if curr_char!='.' and not visited_alphabet:
    #                         if (state, '.') in self.trans.keys():
    #                             stack.put((state, '.'))
    #                         new_alphabet_trans.add(state)
    #                         visited_alphabet = True
    #                     elif curr_char=='.' and
    #                     if curr_char == '.' and (state, '.') in self.trans.keys():
    #                         stack.put((state, '.'))
    #                     elif not visited_alphabet and (state, '.') in self.trans.keys():
    #                         stack.put((state, '.'))
    #                         new_alphabet_trans.add(state)
    #                         visited_alphabet = True

    #             new_trans[(q, c)] = new_alphabet_trans
    #     self.trans = new_trans
    #     self.display()
# ======================================================================
