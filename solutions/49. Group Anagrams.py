class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # n = average length of input strings
        # m = length of input
        
        # sorting each string approach
            # time complexity: O(m*n*log(n))
            # space complexity: O(m*n)
        
        # dic = {}
        # for string in strs:
        #     key = "".join(sorted(string))
        #     if key in dic.keys():
        #         dic[key] = dic[key] + [string]
        #     else:
        #         dic[key] = [string]
        # return dic.values()
        
        
        
        # hash map approach
        # we will use a HashMap for better time complexity
            # time complexity: O(m*n*26) = O(m*n)
            # space complexity O(m*n)
            
        res = defaultdict(list)  # defaultdict handles empty dict edge case

        for word in strs:
            count = [0] * 26  # 26 possible characters

            for ch in word:
                count[ord(ch) - ord("a")] += 1
            
            res[tuple(count)].append(word)
        
        return res.values()

