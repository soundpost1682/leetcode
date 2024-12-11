class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        saw = set()
        for i in range(len(arr)):
            if arr[i]*2 in arr and arr.index(arr[i]*2) != i: return True
        return False


