from Stack import Stack

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
        
        self.lineCount: int = 1
        self.currentLine: str = ''
        self.errorLine: str = ''
        
        self.errorState: str = ''
        self.errorChar:str = ''
        self.errorStack:str = ''
    
    def printError(self):
        print(f'\nInvalid syntax at line {self.lineCount}: ')
        print(self.errorLine)
        
        # print(f'State: {self.errorState}')
        # print(f'Input: {self.errorChar}')
        # print(f'Stack: {self.errorStack}')
    
    def processInput(self, input: str) -> bool:
        while True:
            if self.currentState == '':
                input = input.split('\n')[0]
                self.errorLine = self.currentLine + input
                return False
            elif input == '':
                return (self.stack.Top() == self.startSymbol)
            elif input[0] == '\n':
                self.lineCount += 1
                self.currentLine = ''
                
                # Continue iteration
                input = input[1:]
            elif input[0] != '<' and self.stack.Top() == '<':
                # Continue iteration
                input = input[1:]
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
                
                # Continue iteration
                if newState == '':
                    self.errorState = self.currentState
                    self.errorChar = input[0]
                    self.errorStack = self.stack.Top()
                self.currentState = newState
                self.currentLine += input[0]
                input = input[1:]