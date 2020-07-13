class Solution {
public:
    string defangIPaddr(string address) {
        std::string s = address;
        std::string res = "";
        for (string::size_type i = 0; i < s.length(); i++)
        {
            if (s[i] == '.') {
                res = res + "[.]";
            }
            else
            {
                res = res + s.at(i);
            }
        }
        return res;
    }
};