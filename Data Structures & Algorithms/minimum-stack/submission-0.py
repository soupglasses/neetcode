class MinStack:
    def __init__(self):
        self.stack = []
        self.min_pos = []

    def push(self, elem: int) -> None:
        if not self.stack or elem < self.getMin():
            self.min_pos.append(len(self.stack))
        self.stack.append(elem)

    def pop(self) -> None:
        if not self.stack:
            raise IndexError

        if (len(self.stack) - 1) == self.min_pos[-1]:
            self.min_pos.pop()

        self.stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        if not self.stack:
            raise IndexError

        return self.stack[self.min_pos[-1]]
