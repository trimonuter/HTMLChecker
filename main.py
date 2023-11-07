import Parser
from PDA import PDA

P: PDA = Parser.FileToPDA('0n1n.txt')

inp = input("Type string: ")
acc: bool = P.processInput(inp)

if acc:
    print("String accepted")
else:
    print("String rejected")