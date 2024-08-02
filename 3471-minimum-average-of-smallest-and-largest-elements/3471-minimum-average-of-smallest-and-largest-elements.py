class Solution:
    def minimumAverage(self, nums: List[int]) -> float:
        answer=[]
        for i in range(len(nums)//2):
            n = min(nums)
            x = max(nums)
            nums.remove(n)
            nums.remove(x)
            answer.append((n + x) / 2)
        return min(answer)
