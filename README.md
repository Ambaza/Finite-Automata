# Finite-Automata
Each node represents a state, and transitions between nodes correspond to characters in the input string. Nondeterministic Finite Automata (NFA) allow multiple transitions from one state to another, while Deterministic Finite Automata (DFA) have a unique transition for each input symbol.

The NFAState class represents a state in the NFA, and the NFA class represents the NFA itself. The NFA is constructed by traversing the regex and creating transitions between states. The match method performs a non-deterministic traversal of the NFA to check if there is a match in the input text.

The implementation provided here is a basic example, and for more complex regex patterns, you might need to enhance the construction of the NFA. Additionally, you can convert the NFA to a DFA for more efficient matching.
