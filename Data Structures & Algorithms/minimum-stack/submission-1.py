class MinStack:

    def __init__(self):
        self.s = []
        self.m = []

    def push(self, val: int) -> None:
        self.s.append(val)
        if not self.m:
            self.m.append(val)
            return
        
        if self.m[-1] > val:
            self.m.append(val)
        else:
            self.m.append(self.m[-1])

    def pop(self) -> None:
        self.s.pop()
        self.m.pop()

    def top(self) -> int:
        return self.s[-1]

    def getMin(self) -> int:
        return self.m[-1]
