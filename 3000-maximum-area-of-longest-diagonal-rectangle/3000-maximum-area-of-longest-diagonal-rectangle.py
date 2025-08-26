class Solution:
    def areaOfMaxDiagonal(self, dimensions: List[List[int]]) -> int:
        return max((a*a+b*b, b*a) for a,b in dimensions)[1]



