class Solution:
    def arithmeticTriplets(self, nums: List[int], diff: int) -> int:
        answer =0
        saw = set(nums)
        for i in nums:
            if i + diff in saw and diff*2+i in saw:
                answer +=1
        return answer
        