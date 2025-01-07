class Solution:
    def getSneakyNumbers(self, nums: List[int]) -> List[int]:
        tmp = []
        saw=set()
        for i in nums:
            if i in saw:tmp.append(i)
            else: saw.add(i)
        return tmp
