class Solution:
    def licenseKeyFormatting(self, s: str, k: int) -> str:
        ans = []
        cnt =0
        s2 = s.replace('-', '').upper()
        for i in reversed(range(len(s2))):
            ans.append(s2[i])
            cnt+=1
            if cnt==k and i!=0:
                ans.append('-')
                cnt=0
        return ''.join(ans[::-1])


