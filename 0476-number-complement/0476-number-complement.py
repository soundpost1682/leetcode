class Solution:
    def findComplement(self, num: int) -> int:
        tmp = num.bit_length()
        answer = (1 << tmp) -1
        return num ^ answer

