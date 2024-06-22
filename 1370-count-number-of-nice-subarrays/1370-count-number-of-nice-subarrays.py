class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        answer = cnt = L = 0
        for i in range(len(nums)):
            if nums[i] % 2:
                k -=1
                cnt =0
            while not k:
                k += (nums[L] %2)
                cnt += 1
                L += 1
            answer += cnt
        return answer
