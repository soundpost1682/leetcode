class Solution:
    def isOneBitCharacter(self, bits: List[int]) -> bool:
        i, a = 0, len(bits)
        while i < a-1:
            i += bits[i] +1
        return i== a-1
        
