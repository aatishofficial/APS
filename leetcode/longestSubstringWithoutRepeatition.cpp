// leetcode - https://leetcode.com/problems/longest-substring-without-repeating-characters
class Solution {
public:
    int lengthOfLongestSubstring(string s) {
        int maxLength=0,start=0;
        map<char,int> hash;
        for(int i=0;i<s.size();i++)
        {
            if(hash.find(s[i])!=hash.end() && start<=hash[s[i]])
                start=hash[s[i]]+1;
            else
            {
                maxLength=max(maxLength,i-start+1);
            }
            hash[s[i]]=i;
        }
        return maxLength;
    }
};
