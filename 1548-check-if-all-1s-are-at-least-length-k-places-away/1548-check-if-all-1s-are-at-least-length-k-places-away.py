class Solution:
    def kLengthApart(self, nums: List[int], k: int) -> bool:
        tmp = k
        for i in nums:
            if i == 1:
                if tmp < k:
                    return False
                tmp =0
            else: tmp +=1
        return True
        