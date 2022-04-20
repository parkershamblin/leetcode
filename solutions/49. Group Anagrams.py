class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dic = {}
        for string in strs:
            if "".join(sorted(string)) in dic.keys():
                dic["".join(sorted(string))] = dic["".join(sorted(string))] + [string]
            else:
                dic["".join(sorted(string))] = [string]
        return dic.values()
