class Solution:
    def mergeArrays(self, nums1: List[List[int]], nums2: List[List[int]]) -> List[List[int]]:
        nums1.extend(nums2)
        nums1.sort()
        answer=[]
        for i,v in nums1:
            if answer and answer[-1][0] == i:
                answer[-1][1] += v
            else:
                answer.append([i,v])
        return answer
        