class Solution:
    def countLargestGroup(self, n: int) -> int:
        tmp = defaultdict(int)
        before=0
        for i in range(1, n+1):
            if i % 10==0:
                before = sum(int(i) for i in str(i))
            else:
                before +=1
            tmp[before] +=1
        Xsize= max(tmp.values())
        return sum(1 for j in tmp.values() if j==Xsize)
