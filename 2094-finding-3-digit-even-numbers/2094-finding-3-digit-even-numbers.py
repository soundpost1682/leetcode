class Solution:
    def findEvenNumbers(self, digits: List[int]) -> List[int]:
        ans = set()
        for a,b,c in permutations(digits, 3):
            if a != 0 and c & 1 == 0:
                ans.add(100*a + 10*b + c)
        return sorted(ans)
