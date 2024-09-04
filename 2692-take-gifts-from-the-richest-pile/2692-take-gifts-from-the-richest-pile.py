class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:
        while k > 0:
            maxpile = max(gifts)
            i = gifts.index(maxpile)
            gifts[i] = int(math.sqrt(maxpile))
            k -= 1
        return sum(gifts)
        