class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t): 
            return False
        # useful for only lowercase english characters
        # for follow-up -> to handle unicode characters
        # use hashmap, since the unicode characters are more than 140K characters,
        # average testcases might not include all unicodes, so we don't need to use
        # array for that.
        charmap = [0] * 26

        for i in range(len(s)):
            charmap[(ord(s[i]) - ord('a'))] += 1
            charmap[(ord(t[i]) - ord('a'))] -= 1

        return all(freq == 0 for freq in charmap)
        