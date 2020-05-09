# leetcode - https://leetcode.com/problems/range-sum-query-immutable/
class NumArray:

    def __init__(self, nums: List[int]):
        self.n=nums

    def sumRange(self, i: int, j: int) -> int:
        res=0
        for k in range(i,j+1):
            res+=self.n[k]
        return res


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(i,j)
