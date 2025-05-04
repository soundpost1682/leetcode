class Solution:
    def numEquivDominoPairs(self, dominoes: List[List[int]]) -> int:
        cnt = Counter()
        ans =0
        for i,v in dominoes:
            tmp = tuple(sorted([i,v]))
            if tmp in cnt:
                ans+=cnt[tmp]
            cnt[tmp] +=1
        return ans
        
