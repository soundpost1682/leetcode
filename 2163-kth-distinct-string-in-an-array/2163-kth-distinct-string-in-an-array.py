class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        tmp=[]
        for i in arr:
            if arr.count(i) == 1:
                tmp.append(i)
        return '' if k>len(tmp) else tmp[k-1]
