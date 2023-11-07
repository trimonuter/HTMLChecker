from stack import Stack
from copy import deepcopy

class PDA:
    def __init__(self, states, alphabet, stackSymbols, transitions, startState, startSymbol) -> None:
        self.states: list[str] = states
        self.alphabet: list[str] = alphabet
        self.stackSymbols: list[str] = stackSymbols
        self.transitions = transitions
        self.startState: str = startState
        self.startSymbol: str = startSymbol
        
        self.stack: Stack = Stack(startSymbol)
        self.currentStates: list[str] = [startState]
    
    def processInput(self, input: str) -> bool:
        if input == '':
            return (self.stack.Top() == self.startSymbol)
        else:
            # Clear current states
            states = deepcopy(self.currentStates)
            self.currentStates.clear()
            
            # Transition
            char: str = input[0]
            for state in states:
                if char in self.transitions[state]:
                    top = self.stack.Top()
                    if top in self.transitions[state][char]:
                        Transition = self.transitions[state][char][top]
                        newState = Transition[0]
                        newTop = Transition[1]
                        
                        self.currentStates.append(newState)
                        self.stack.Pop()
                        self.stack.Push(newTop)
            
            return self.processInput(input[1:])
           
t = {
    'q': {
        '0': {
            'Z': ['q', 'Z0'],
            '0': ['q', '00']
        },
        '1': {
            '0': ['p', '']
        }
    },
    'p': {
        '1': {
            '0': ['p', '']
        },
        '': {
            'Z': ['p', '']
        }
    }
}

p: PDA = PDA(['q', 'p'], ['0', '1'], ['Z, 0'], t, 'q', 'Z')

inp = input("Type string: ")
acc: bool = p.processInput(inp)
if acc:
    print("String accepted")
else:
    print("String rejected")