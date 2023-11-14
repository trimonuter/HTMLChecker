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
        self.currentState: str = startState
    
    def processInput(self, input: str) -> bool:
        if self.currentState == '':
            return False
        elif input == '':
            return (self.stack.Top() == self.startSymbol)
        # elif input[0] in [' ', '\n']:
        #     return self.processInput(input[1:])
        elif input[0] != '<' and self.stack.Top() == '<':
            return self.processInput(input[1:])
        else:
            # Initialize state and newState
            state = self.currentState
            newState = ''
            
            # Transition
            char: str = input[0]
            if char in self.transitions[state]:
                top = self.stack.Top()
                if top in self.transitions[state][char]:
                    Transition = self.transitions[state][char][top]
                    newState = Transition[0]
                    newTop = Transition[1]
                    
                    self.stack.Pop()
                    self.stack.Push(newTop)
                else:
                    if '%' in self.transitions[state]:
                        top = self.stack.Top()
                        if top in self.transitions[state]['%']:
                            Transition = self.transitions[state]['%'][top]
                            newState = Transition[0]
                            newTop = Transition[1]
                            
                            self.stack.Pop()
                            self.stack.Push(newTop)
            else:
                if '%' in self.transitions[state]:
                    top = self.stack.Top()
                    if top in self.transitions[state]['%']:
                        Transition = self.transitions[state]['%'][top]
                        newState = Transition[0]
                        newTop = Transition[1]
                        
                        self.stack.Pop()
                        self.stack.Push(newTop)
                    elif '%' in self.transitions[state]['%']:
                        Transition = self.transitions[state]['%']['%']
                        newState = Transition[0]
                        newTop = Transition[1]
                        
                        self.stack.Pop()
                        self.stack.Push(newTop)
                    
            self.currentState = newState
            return self.processInput(input[1:])
           
# t = {
#     'q': {
#         '0': {
#             'Z': ['q', 'Z0'],
#             '0': ['q', '00']
#         },
#         '1': {
#             '0': ['p', '']
#         }
#     },
#     'p': {
#         '1': {
#             '0': ['p', '']
#         },
#         '': {
#             'Z': ['p', '']
#         }
#     }
# }