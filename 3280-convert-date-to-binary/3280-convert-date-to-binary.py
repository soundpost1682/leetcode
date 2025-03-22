class Solution:
    def convertDateToBinary(self, date: str) -> str:
        y, m, d = date.split('-')
        yy = bin(int(y))[2:]
        mm = bin(int(m))[2:]
        dd = bin(int(d))[2:]
        return f'{yy}-{mm}-{dd}'
