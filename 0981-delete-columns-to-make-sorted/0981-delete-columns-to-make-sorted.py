class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        ans=0
        for c in map(list, zip(*strs)):
            if c != sorted(c):
                ans+=1
        return ans
        
