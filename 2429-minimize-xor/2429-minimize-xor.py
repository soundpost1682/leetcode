class Solution:
    def minimizeXor(self, num1: int, num2: int) -> int:
        tmp = num1.bit_count() - num2.bit_count()
        if tmp > 0:
            for _ in range(tmp):
                num1 &= num1 -1
        else:
            for _ in range(-tmp):
                num1 |= num1 +1
        return num1
        