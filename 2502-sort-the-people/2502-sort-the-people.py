class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        return [v for i, v in sorted(zip(heights, names), reverse=True)]