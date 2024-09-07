class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        saw=set()
        for n in nums:
            if n in saw:
                return True
            saw.add(n)
        return False
        