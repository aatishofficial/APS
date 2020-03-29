class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        m={}
        for i in len(nums):
            remain=target-nums[i]
            if remain in m:
                return i,m[remain]
            else:
                m[nums[i]]=i
        return []
