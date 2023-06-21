from finite_automata.finite_automata import FiniteAutomata


class DefiniteFiniteAutomata(FiniteAutomata):
    def __init__(self, states=None, alphabet=None, init_state=None, accepting=None, trans=None) -> None:
        super().__init__(states, alphabet, init_state, accepting, trans)
