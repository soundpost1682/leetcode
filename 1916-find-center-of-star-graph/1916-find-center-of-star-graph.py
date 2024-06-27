class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        l, r= edges[0], edges[1]
        return l[0] if l[0] in r else l[1]
        