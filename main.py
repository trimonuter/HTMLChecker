import Parser
from PDA import PDA
from yaml import dump

P: PDA = Parser.FileToPDA('PDA.txt')
# print(dump(P.transitions['html']['h']))
# print(P.transitions['html']['h'])

# inp = input("Type string: ")
htmlfile = 'tes5.html'
with open(htmlfile, 'r') as file:
    inp = file.read()
    print(f'Reading {htmlfile}...')
    print(f'Input:\n{inp}')
acc: bool = P.processInput(inp)

if acc:
    print("String accepted")
else:
    print("String rejected")