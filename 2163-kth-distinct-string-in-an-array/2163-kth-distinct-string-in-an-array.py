class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        tmp ={}
        for i in arr:
            tmp[i] = tmp.get(i, 0) +1
        for j in arr:
            if tmp[j] ==1:
                k -=1
            if k==0:
                return j
        return ''
        