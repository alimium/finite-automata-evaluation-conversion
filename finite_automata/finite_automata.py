import graphviz


class FiniteAutomata:
    def __init__(self, states=None, alphabet=None, init_state=None, accepting=None, trans=None) -> None:
        self.states = [i for i in range(
            states)] if states is not None else None
        self.alphabet = alphabet
        self.init_state = init_state
        self.accepting = accepting
        self.trans = trans

        # TODO: Error handling upon invalid constructor input



    def display(self):
        # Create a new Graphviz graph
        dot = graphviz.Digraph()

        # Add the states to the graph
        if self.states is not None:
            for state in self.states:
                if state == self.init_state:
                    dot.node(str(state), shape="circle", style="bold", label=f"init\n{self.init_state}")
                elif self.accepting is not None and state in self.accepting:
                    dot.node(str(state), shape="circle", peripheries="2")
                else:
                    dot.node(str(state), shape="circle")

        # Add the transitions to the graph
        if self.trans is not None:
            for transition in self.trans:
                dot.edge(str(transition[0]), str(transition[2]), label=transition[1])

        # Render the graph to a PNG image
        dot.render("figures/automata", format="png", view=True) 