class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        L,R=0,0
        hasmap = dict()
        maxlength = float("-inf")
        for R in range(len(s)):
            hasmap[s[R]] = 1 + hasmap.get(s[R], 0)
            most_freq = max(hasmap.values())
            while ((R-L+1) - most_freq) > k:
                hasmap[s[L]] -= 1
                L += 1
            maxlength = max(maxlength, R-L+1)
        return maxlength
        