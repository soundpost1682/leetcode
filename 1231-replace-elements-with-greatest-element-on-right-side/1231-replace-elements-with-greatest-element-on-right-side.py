class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        tmp = -1
        for i in range(len(arr)-1, -1, -1):
            if arr[i] > tmp:
                tmp, arr[i] = arr[i], tmp
            else:
                arr[i] = tmp
        return arr

