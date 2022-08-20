class Solution {
public:
    int threeSumMulti(vector<int>& arr, int target) {
        int n = arr.size();
        int MOD = 1e9 + 7;
        vector<vector<int>> dp(target+1, vector<int>(4));
        dp[0][0] = 1;
        
        for(auto num: arr){
            for(int t=target; t>=0; t--){
                for(int cnt=2; cnt>=0; cnt--){
                    // num + x = t
                    // x = t - num
                    if(t - num < 0) continue;
                    dp[t][cnt+1] = (dp[t][cnt+1] + dp[t-num][cnt]) % MOD;
                }
            }
        }
        
        return dp[target][3];
    }
};
