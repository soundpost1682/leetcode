class Solution:
    def maxKelements(self, nums: List[int], k: int) -> int:
        tmp = [-i for i in nums]
        heapify(tmp)
        res = 0
        for i in range(k):
            res -= tmp[0]
            heapreplace(tmp, tmp[0]//3)
        return res
