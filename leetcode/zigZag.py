# leetcode - https://leetcode.com/problems/zigzag-conversion
class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows==1 or numRows>=len(s):
            return s
        arr=[''] * numRows
        index,step=0,1
        for c in s:
            arr[index] += c
            if index==0:
                step=1
            if index==numRows-1:
                step=-1
            index += step
           
        return ''.join(arr)
