class Solution:
    def numEquivDominoPairs(self, dominoes: List[List[int]]) -> int:
        cnt = defaultdict(int)
        ans =0
        for i,v in dominoes:
            cnt[1<<i | 1<<v] +=1
        for z in cnt.values():
            ans += z * (z-1)
        return ans // 2
        