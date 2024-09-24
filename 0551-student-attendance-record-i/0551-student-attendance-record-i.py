class Solution:
    def checkRecord(self, s: str) -> bool:
        return False if 'LLL' in s or s.count('A') >=2 else True
        
