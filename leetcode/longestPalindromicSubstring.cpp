// leetcode - https://leetcode.com/problems/longest-palindromic-substring
class Solution {
public:
    string longestPalindrome(string s) {
        if(s.size()==0)
            return "";
        int n=s.size();
        bool table[n][n];
        for(int i=0;i<n;i++)
        {
            for(int j=0;j<n;j++)
                table[i][j]=false;
        }
        for(int i=0;i<n;i++)
            table[i][i]=true;
        int start=0,maxlength=1;
        for(int i=0;i<n-1;i++)
        {
            if(s[i]==s[i+1])
            {
                table[i][i+1]=true;
                start=i;
                maxlength=2;
            }
        }
        for(int k=3;k<=n;k++)
        {
            for(int i=0;i<n-k+1;i++)
            {
                int j=i+k-1;
                if(table[i+1][j-1] && s[i]==s[j])
                {
                    table[i][j]=true;
                    if(k>maxlength)
                    {
                        start=i;
                        maxlength=k;
                    }
                }
            }
        }
        string res="";
        for(int i=start;i<=start+maxlength-1;i++)
            res+=s[i];
        return res;
    }
};
