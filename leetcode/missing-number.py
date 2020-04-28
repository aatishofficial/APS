# leetcode - https://leetcode.com/problems/missing-number/
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n=len(nums)
        t=0
        for i,num in enumerate(nums):
            t^=(num ^ i)
        return n^t
