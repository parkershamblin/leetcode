class Solution {
public:
    vector<int> sumZero(int n) {
        vector<int> res{ };
        res.push_back(-n + 1);
        for (int i{1}; i < n; i++) {
            res.push_back(res.at(i-1) + 2);
        };
        return res;
    }
};
