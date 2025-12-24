class Solution:
    def minimumBoxes(self, apple: List[int], capacity: List[int]) -> int:
        tmp = sum(apple)
        for i,j in enumerate(sorted(capacity, reverse=True)):
            tmp -= j
            if tmp <=0 : return i+1
        return -1
        