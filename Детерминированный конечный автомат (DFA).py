class DFA:
    def __init__(self, states, alphabet, transitions, start_state, accept_states):
        self.states = states
        self.alphabet = alphabet
        self.transitions = transitions
        self.start_state = start_state
        self.accept_states = accept_states

    def process(self, input_string):
        current_state = self.start_state
        for symbol in input_string:
            if symbol not in self.alphabet:
                return False
            key = (current_state, symbol)
            if key not in self.transitions:
                return False
            current_state = self.transitions[key]
        return current_state in self.accept_states

# Пример использования
states = {'q0', 'q1', 'q2'}
alphabet = {'a', 'b'}
transitions = {
    ('q0', 'a'): 'q1',
    ('q1', 'b'): 'q2',
    ('q2', 'a'): 'q2',
    ('q2', 'b'): 'q2',
}
start_state = 'q0'
accept_states = {'q2'}

dfa = DFA(states, alphabet, transitions, start_state, accept_states)
print(dfa.process("ab"))   # True
print(dfa.process("a"))    # False
print(dfa.process("abb"))  # True