class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        # sort the list of strings, based on length
        strs.sort(key=len)
        prefix = strs[0]
        for i in range(1, len(strs)):
            if prefix == "": return prefix
            for j in range(len(prefix)):
                if prefix[j] != strs[i][j]:
                    prefix = prefix[:j]
                    break
        return prefix



        