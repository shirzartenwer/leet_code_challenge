# https://neetcode.io/problems/minimum-stack

#  requirements: each method should be O(1) time complexity and can be O(n) complexity
class TwoStack:

    def __init__(self):
        self.item = []
        # The minimum stack only stores the minimum value
        self.minStack = []

    def push(self, val: int) -> None:
        self.item.append(val)
        val = min(val, self.minStack[-1] if self.minStack else val)
        self.minStack.append(val)

    def pop(self) -> None:
        self.item.pop()
        self.minStack.pop()

    def top(self) -> int:
        return self.item[-1]

    def getMin(self) -> int:
        return self.minStack[-1]
