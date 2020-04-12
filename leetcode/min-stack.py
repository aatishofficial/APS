# leetcode - https://leetcode.com/problems/min-stack
class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []

    def push(self, x: int) -> None:
        cur=self.getMin()
        if cur==None or x<cur:
            cur=x
        self.stack.append((x,cur))

    def pop(self) -> None:
        self.stack.pop()


    def top(self) -> int:
        if len(self.stack)==0:
            return None
        else:
            return self.stack[-1][0]

    def getMin(self) -> int:
        if len(self.stack)==0:
            return None
        else:
            return self.stack[-1][1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
