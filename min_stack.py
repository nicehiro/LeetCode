class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.memory = []
        self.min = []

    def push(self, x: int) -> None:
        self.memory.append(x)
        if len(self.memory) == 1:
            self.min.append(x)
        else:
            self.min.append(min(self.min[-1], x))

    def pop(self) -> None:
        if len(self.memory) <= 0:
            return
        self.memory.pop(-1)
        self.min.pop(-1)

    def top(self) -> int:
        if len(self.memory) <= 0:
            return None
        return self.memory[-1]

    def getMin(self) -> int:
        if len(self.memory) <= 0:
            return None
        return self.min[-1]


if __name__ == '__main__':
    # Your MinStack object will be instantiated and called as such:
    x = 3
    stack = MinStack()
    stack.push(-2)
    stack.push(0)
    stack.push(-3)
    print(stack.getMin())
    stack.pop()
    print(stack.top())
    print(stack.getMin())
