// leetcode - https://leetcode.com/problems/zigzag-conversion
class Solution {
public:
    string convert(string s, int numRows) {
        string arr[numRows];
        int count=0;
        int increasing=1;
        for(int i=0;i<s.size();i++)
        {
            if(increasing==1)
            {
                arr[count++]+=s[i];
                if(numRows>2 && count==numRows)
                {
                    increasing=0;
                    count--;
                } 
                else if(count==numRows)
                    count=0;
            }
            else
            {
                if(count-1>=0)
                    count--;
                arr[count]+=s[i];
                if(count==1)
                {
                    increasing=1;
                    count=0;
                }
            }
        }
        string res;
        for(int i=0;i<numRows;i++)
        {
            for(int j=0;j<arr[i].size();j++)
                res+=arr[i][j];
        }
        return res;
    }
};
