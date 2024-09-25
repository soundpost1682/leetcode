class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        left, right, L = 0, -1, len(arr)
        while left < L-1 and arr[left] < arr[left+1]:
            left +=1
        while right > -L and arr[right] < arr[right-1]:
            right -=1
        return left == right + L and 0<left and right < -1
