import Parser
from PDA import PDA

P: PDA = Parser.FileToPDA('PDA.txt')
# htmlfile = 'tesAllKomentar.html'
htmlfile = 'debug.html'
with open(htmlfile, 'r') as file:
    inp = file.read()
    print(f'Reading {htmlfile}...')
    print(f'Input:\n{inp}')
acc: bool = P.processInput(inp)

print('\n------------------------------------------------')
if acc:
    print("Accepted!")
else:
    print("Rejected: Syntax Error")
    P.printError()
print('------------------------------------------------')