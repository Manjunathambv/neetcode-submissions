import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        l, r = 1, max(piles)
        result = r
        while l <= r:
            k = (l + r) // 2
            hours_req = 0
            for pile in piles:
                hours_req += math.ceil(float(pile) / k)
            if hours_req <= h:
                result = k
                r = k - 1
            else:
                l = k + 1
        return int(result)