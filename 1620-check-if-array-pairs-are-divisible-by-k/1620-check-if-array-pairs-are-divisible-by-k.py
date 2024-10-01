class Solution:
    def canArrange(self, arr: List[int], k: int) -> bool:
        tmp = [0] * k
        for n in arr:
            remain = (n % k + k) % k
            tmp[remain] += 1
        if tmp[0] % 2 != 0: return False
        for i in range(1, k//2+1):
            if tmp[i] != tmp[k-i]: return False
        return True
