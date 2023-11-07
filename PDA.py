class PDA:
    def __init__(self, states, alphabet, stackSymbols, transitions, startState, startSymbol) -> None:
        self.states = states
        self.alphabet = alphabet
        self.stackSymbols = stackSymbols
        self.transitions = transitions,
        self.startState = startState,
        self.startSymbol = startSymbol