from typing import TextIO
from yaml import dump

from PDA import PDA

def ADVNEWLINE(file: TextIO) -> list[str]:
    return [x.replace('$', '').replace('W', ' ') for x in file.readline().strip().split(' ')]

def FileToPDA(filename: str) -> PDA:
    with open(filename) as file:
        # Line 1: States
        states = ADVNEWLINE(file)
        # print(states)
        
        # Line 2: Alphabet
        alphabet = ADVNEWLINE(file)
        # print(alphabet)
        
        # Line 3: Symbols
        symbols = ADVNEWLINE(file)
        # print(symbols)
        
        # Line 4: Start State
        startState = ADVNEWLINE(file)[0]
        # print(startState)
        
        # Line 5: Start Symbol
        startSymbol = ADVNEWLINE(file)[0]
        # print(startSymbol)
        
        # Line 6: PDA Type
        PDAType = ADVNEWLINE(file)[0]
        # print(PDAType)
        
        line = ADVNEWLINE(file)
        t = {}
        while line[0] != '':
            while line[0] == '#':
                line = ADVNEWLINE(file)
            InitialState = line[0]
            Input = line[1]
            TopStack = line[2]
            Destination = line[3:]
            Destination[1] = Destination[1][::-1]
            
            transition = {
                Input: {
                    TopStack: Destination
                }
            }
            if InitialState not in t:
                t[InitialState] = transition
            else:
                if Input not in t[InitialState]:
                    t[InitialState][Input] = transition[Input]
                else:
                    if TopStack not in t[InitialState][Input]:
                        t[InitialState][Input][TopStack] = transition[Input][TopStack]
                        
            line = ADVNEWLINE(file)
            
        # print(t)
        P: PDA = PDA(states, alphabet, symbols, t, startState, startSymbol)
        return P
    
    
# {   'q': 
#         {'0': {
#             'Z': [[['q', 'Z0']]], 
#             '0': [[['q', '00']]]
#         }, 
#         '1': {
#             '0': [[['p', '$']]]
#             }
#         }, 
#     'p': 
#         {'1': {'0': [[['p', '$']]]}, '$': {'Z': [[['p', '$']]]}
#          }
# }