# leetcode - https://leetcode.com/problems/intersection-of-two-arrays-ii/
class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        m=collections.defaultdict(int)
        for n in nums1:
            m[n]+=1
        res=[]
        for n in nums2:
            if n in m and m[n]>0:
                res.append(n)
                m[n]-=1
        return res
