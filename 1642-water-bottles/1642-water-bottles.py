class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        tmp =0
        while numBottles >= numExchange :
            tmp += numExchange
            numBottles -= numExchange

            numBottles += 1
        return tmp + numBottles
        