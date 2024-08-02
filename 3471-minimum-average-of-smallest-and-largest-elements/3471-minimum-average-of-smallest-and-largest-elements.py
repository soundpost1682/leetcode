class Solution:
    def minimumAverage(self, nums: List[int]) -> float:
        answer = []
        while nums != []:
            a = min(nums)
            b = max(nums)
            answer.append((a+b) / 2)
            nums.remove(a)
            nums.remove(b)
        return min(answer)
