class Stack:
    def __init__(self, start: str) -> None:
        self.stack: str = start
    
    def Top(self) -> str:
        n: int = len(self.stack)
        return self.stack[n - 1] 
    
    def Push(self, word: str) -> None:
        self.stack += word
        
    def Pop(self) -> None:
        self.stack = self.stack[:-1]
        
# s: Stack = Stack("X")
# cmd = ''

# while (cmd != 'EXIT'):
#     print(f"\nCurrent stack: {s.stack}")
#     cmd = input("Input command (TOP / PUSH / POP / EXIT): ")
    
#     if cmd == 'TOP':
#         print(f"Top: {s.Top()}")
#     elif cmd == 'PUSH':
#         push = input("String to push: ")
#         s.Push(push)
#     elif cmd == 'POP':
#         s.Pop()