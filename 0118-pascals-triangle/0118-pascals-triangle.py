class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        return [[comb(a,b) for b in range(a+1)] for a in range(numRows)]

