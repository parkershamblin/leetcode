class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        int m,n;
        
        //creating and inserting values in hashmap
        unordered_map<int,int> map;
        for(auto x: nums) map[x]++;
        
        //to get the first element index
        for(int i = 0; i<nums.size() ; i++)
        {
            map[nums[i]]--;
            if(map[nums[i]]==0) map.erase(nums[i]);
            if(map.find(target-nums[i])!=map.end())
            {
                m = i;
                break;
            }
        }
        //to get second element index
        for(int i = 0; i<nums.size() ; i++)
        {
            if(nums[i] + nums[m]==target && m!=i)
            {
                n = i;
                break;
            }
        }
        return {m,n};
    }
};
