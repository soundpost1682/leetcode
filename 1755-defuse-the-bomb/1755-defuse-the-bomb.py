class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:
        if k == 0: return [0 for i in code]
        tmp = code
        code2 = code * 2
        for i in range(len(tmp)):
            if k > 0:
                tmp[i] = sum(code2[i+1 : i+k+1])
            else :
                tmp[i] = sum(code2[i+len(tmp) + k : i+len(tmp)])
        return tmp

