class Solution:
    def findClosest(self, x: int, y: int, z: int) -> int:
        tmp1 = abs(x-z)
        tmp2 = abs(y-z)
        if tmp1 < tmp2 : return 1
        elif tmp2 < tmp1 : return 2
        else : return 0
        