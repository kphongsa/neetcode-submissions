class MinStack:

    def __init__(self):
        self.stack = []
        self.min_stack = [2147483647]

    def push(self, val: int) -> None:
        self.stack.append(val)

        small = min(self.stack[-1], self.min_stack[-1])
        self.min_stack.append(small)

        
    def pop(self) -> None:
        self.stack.pop()
        self.min_stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min_stack[-1]
