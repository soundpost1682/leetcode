class Solution:
    def canAliceWin(self, nums: List[int]) -> bool:
        sing = sum(s for s in nums if s < 10)
        db = sum(d for d in nums if d > 9)
        return True if sing > db or sing < db else False
