class Solution:
    def stableMountains(self, height: List[int], threshold: int) -> List[int]:
        ans=[]
        for i, (pre, mt) in enumerate(pairwise(height)):
            if pre > threshold : 
                ans.append(i+1)
        return ans
        