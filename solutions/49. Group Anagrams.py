class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dic = {}
        for string in strs:
            key = "".join(sorted(string))
            if key in dic.keys():
                dic[key] = dic[key] + [string]
            else:
                dic[key] = [string]
        return dic.values()
​
