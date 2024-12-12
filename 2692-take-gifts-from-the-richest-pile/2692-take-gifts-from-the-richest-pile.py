class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:
        while k:
            gifts.sort(reverse=True)
            pi = gifts[0]
            gifts.pop(0)
            gifts.append(int(sqrt(pi)))
            k -=1
            # maxpile = max(gifts)
            # i = gifts.index(maxpile)
            # gifts[i] = int(math.sqrt(maxpile))
            # k -= 1
        return sum(gifts)
        