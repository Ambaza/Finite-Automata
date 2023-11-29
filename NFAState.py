class NFAState:
    def __init__(self, label):
        self.label = label
        self.transitions = {}

class NFA:
    def __init__(self, regex):
        self.start_state = NFAState("start")
        self.accept_state = NFAState("accept")
        self.regex = regex

        self.build_nfa()

    def build_nfa(self):
        current_state = self.start_state

        for char in self.regex:
            if char == '*':
                current_state.transitions[self.accept_state] = current_state
            else:
                new_state = NFAState(char)
                current_state.transitions[new_state] = new_state
                current_state = new_state

        current_state.transitions[self.accept_state] = self.accept_state

    def match(self, text):
        current_states = set([self.start_state])

        for char in text:
            next_states = set()

            for state in current_states:
                next_states.update(state.transitions.get(char, set()))

            current_states = next_states

        return self.accept_state in current_states

# Example usage:
nfa_regex = 'a*b'
nfa_engine = NFA(nfa_regex)

print(nfa_engine.match("aaab"))  # Should match
print(nfa_engine.match("cb"))    # Should not match
