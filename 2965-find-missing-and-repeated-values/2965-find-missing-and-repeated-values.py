class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        ans, cnt = [0,0], Counter(chain(*grid))
        n = len(cnt)+1
        for i in range(1, n+1):
            if cnt[i] == 1: continue
            ans[1-cnt[i]//2] = i
        return ans
