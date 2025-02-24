class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        return [[abs(j-1) for j in i][::-1] for i in image]
