class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        tmp = {}
        answer=[]
        for i in nums1:
            if i not in tmp: tmp[i] = 1
            else: tmp[i] += 1
        for j in nums2:
            if j in tmp and tmp[j] > 0:
                answer.append(j)
                tmp[j] -= 1
        return answer


                