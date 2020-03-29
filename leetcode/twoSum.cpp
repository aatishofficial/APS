/* https://leetcode.com/problems/two-sum/    */

class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        unordered_map<int,int> hash;
        vector<int> res;
        for(int i=0;i<nums.size();i++)
        {
            int remain=target-nums[i];
            if(hash.find(remain)!=hash.end())
            {
                res.push_back(hash[remain]);
                res.push_back(i);
                return res;
            }
            hash[nums[i]]=i;
        }
        return res;
    }
};
