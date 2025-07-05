class Solution:
    def findLucky(self, arr: List[int]) -> int:
        tmp =Counter(arr)
        ans =-1
        for i,j in tmp.items():
            if i==j:
                ans = max(ans, i)
        return ans
        