# leetcode - https://leetcode.com/problems/letter-combinations-of-a-phone-number/
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        d={'2':['a','b','c'],'3':['d','e','f'],'4':['g','h','i'],'5':['j','k','l'],'6':['m','n','o'],'7':['p','q','r','s'],'8':['t','u','v'],'9':['w','x','y','z']}
        
        def back(combination,digits):
            if len(digits)==0:
                res.append(combination)
            else:
                for letter in d[digits[0]]:
                    back(combination+letter,digits[1:])
        res=[]
        if digits:
            back("",digits)
        return res
