# leetcode - https://leetcode.com/problems/count-primes/
class Solution:
    def countPrimes(self, n: int) -> int:
        if n<=1:
            return 0
        arr=[1]*n
        arr[0]=0
        arr[1]=0
        for i in range(2,int(n**0.5)+1):
            if arr[i]==1:
                j=2
                while i*j<n:
                    arr[i*j]=0
                    j+=1
        return sum(arr)
