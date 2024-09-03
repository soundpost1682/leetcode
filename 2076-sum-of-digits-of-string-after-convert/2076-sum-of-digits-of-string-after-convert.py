class Solution:
    def getLucky(self, s: str, k: int) -> int:
        s = ''.join(str(ord(ch) - 96) for ch in s)
        for i in range(k):
            s = str(sum(int(ch) for ch in s))
        return int(s)

