class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        saw = set(nums)
        tmp,cnt = 0,0
        for i in saw:
            tmp2 = nums.count(i)
            if tmp == tmp2:
                cnt +=1
            elif tmp < tmp2:
                tmp = tmp2
                cnt = 1
        return tmp * cnt
        

