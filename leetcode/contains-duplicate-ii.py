# leetcode - https://leetcode.com/problems/contains-duplicate-ii/
class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        h={}
        for i,num in enumerate(nums):
            if num in h and i-h[num] <=k:
                return True
            h[num]=i
        return False
