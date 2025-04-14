from collections import deque

class MyQueue:
    def __init__(self):
        self.stack1 = deque()
        self.stack2 = deque()

    def push(self, x: int) -> None:
        self.stack1.append(x)
        
    def pop(self) -> int:
        if not self.stack2:
            self._transfer()
        
        return self.stack2.pop()
        
    def peek(self) -> int:
        if not self.stack2:
            self._transfer()
            
        return self.stack2[-1]
    
    def empty(self) -> bool:
        return len(self.stack1) == 0 and len(self.stack2) == 0
    
    def _transfer(self) -> None:
        while self.stack1:
            self.stack2.append(self.stack1.pop())
