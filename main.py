import Parser
from PDA import PDA
from yaml import dump

P: PDA = Parser.FileToPDA('PDA.txt')
# print(dump(P.transitions['html']['h']))
# print(P.transitions['html']['h'])

inp = input("Type string: ")
acc: bool = P.processInput(inp)

if acc:
    print("String accepted")
else:
    print("String rejected")