class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles.sort()
        max_coin = 0
        n = len(piles)
        i = n // 3
        while i < n:
            max_coin += piles[i]
            i += 2
        return max_coin
