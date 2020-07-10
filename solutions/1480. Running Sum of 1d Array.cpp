class Solution {
public:
    vector<int> runningSum(vector<int>& nums) {
        int sum = 0;
        vector<int> res;
        for (size_t i = 0; i < nums.size(); i++)
        {
            sum = sum + nums.at(i);
            res.push_back(sum);
        }        
        return res;
    }
};