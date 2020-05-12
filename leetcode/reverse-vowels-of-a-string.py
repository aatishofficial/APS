# leetcode - https://leetcode.com/problems/reverse-vowels-of-a-string/
class Solution:
    def reverseVowels(self, s: str) -> str:
        left,right=0,len(s)-1
        vowel=['a','e','i','o','u','A','E','I','O','U']
        s=list(s)
        while left<right:
            if s[left] in vowel and s[right] in vowel:
                s[left],s[right]=s[right],s[left]
                left,right=left+1,right-1
            elif s[left] in vowel:
                right=right-1
            elif s[right] in vowel:
                left=left+1
            else:
                left,right=left+1,right-1
        return ''.join(s)
