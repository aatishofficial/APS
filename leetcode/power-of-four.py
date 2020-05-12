# leetcode - https://leetcode.com/problems/power-of-four
class Solution:
    def isPowerOfFour(self, num: int) -> bool:
        mask = 0b01010101010101010101010101010101
        if num<=0:
            return False
        if num & num-1 != 0:
            return False
        if num & mask != 0:
            return True
        return False
