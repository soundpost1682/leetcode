class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        L=len(arr)
        a,b = 0, L-1
        if L < 3 : return False

        while a < L-1 and arr[a] < arr[a+1] : a+=1

        while b > 0 and arr[b] < arr[b-1] : b-=1
        # print(a, b)
        if a == L-1 or a==0: return False
        return a==b
