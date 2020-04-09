# leetcode - https://leetcode.com/problems/gas-station
class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        ret,s,cur=0,0,0
        for i in range(len(gas)):
            cur+=(gas[i]-cost[i])
            s+=(gas[i]-cost[i])
            if cur<0:
                cur=0
                ret=i+1
        return -1 if s<0 else ret
