class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        arr.sort()
        dif = [arr[i+1] - arr[i] for i in range(len(arr)-1)]
        tmp = min(dif)
        return [[arr[i], arr[i+1]] for i,v in enumerate(dif) if v==tmp]
        