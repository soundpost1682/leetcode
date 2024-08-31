class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        tmp =Counter(arr)
        for i in arr:
            if tmp[i] == 1:
                k -=1
                if k ==0:
                    return i
        return ''
        