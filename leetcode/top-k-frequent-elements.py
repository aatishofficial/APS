# leetcode - https://leetcode.com/problems/top-k-frequent-elements/
import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq={}
        freq_list=[]
        for num in nums:
            if num in freq:
                freq[num]=freq[num]+1
            else:
                freq[num]=1
        for key in freq.keys():
            freq_list.append((-freq[key],key))
        heapq.heapify(freq_list)
        res=[]
        for i in range(0,k):
            res.append(heapq.heappop(freq_list)[1])
        return res
