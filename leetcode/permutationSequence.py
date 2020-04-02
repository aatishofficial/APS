# leetcode - https://leetcode.com/problems/permutation-sequence/
class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        nums=list(range(1,n+1))
        permutation=''
        k-=1
        while n>0:
            n-=1
            index,k=divmod(k,math.factorial(n))
            permutation+=str(nums[index])
            nums.remove(nums[index])
        return permutation
