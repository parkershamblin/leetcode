class Solution {
public:
    vector<int> runningSum(vector<int>& nums) {
        vector<int> run_sum={nums.at(0)};
        for (int i{1}; i < nums.size(); i++) {
            run_sum.push_back(run_sum.at(i-1) + nums.at(i));
        };
        return run_sum;
    }
};
