class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        L=len(arr)
        a,b = 1, L-1
        if len(arr) < 3: return False
        while a < L and arr[a] > arr[a-1]:
            a +=1
        while b > 0 and arr[b] < arr[b-1]:
            b -=1
        a -=1
        if a == L-1 or a==0: return False
        return a==b

