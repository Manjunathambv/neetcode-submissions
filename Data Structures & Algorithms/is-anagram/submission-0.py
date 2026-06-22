class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        ch_ar = [0] * 256
        for ch in s:
            index = ord(ch)
            ch_ar[index] += 1
        for ch in t:
            index = ord(ch)
            if ch_ar[index] != 0:
                ch_ar[index] -= 1
            else:
                ch_ar[index] += 1

        if sum(ch_ar) != 0:
            return False
        return True