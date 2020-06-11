# leetcode - https://leetcode.com/problems/random-pick-with-weight/
import random,bisect
class Solution:

    def __init__(self, w: List[int]):
        self.v=[]
        self.v.append(w[0])
        for i in range(1,len(w)):
            self.v.append(self.v[-1]+w[i])

    def pickIndex(self) -> int:
        r=random.randint(0,self.v[-1]-1)
        return bisect.bisect_right(self.v,r)


# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()
