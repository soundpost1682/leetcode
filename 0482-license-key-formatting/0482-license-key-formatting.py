class Solution:
    def licenseKeyFormatting(self, s: str, k: int) -> str:
        tmp = s.replace('-','').upper()
        ans1 = len(tmp) % k
        reform = tmp[:ans1]
        
        for i in range(ans1, len(tmp), k):
            if reform:
                reform += '-'
            reform += tmp[i:i+k]
        return reform
        
