class Solution:
    def removeAnagrams(self, words: List[str]) -> List[str]:
        tmp = [''.join(sorted(i)) for i in words]
        ans = [words[0]]

        for i in range(1, len(words)):
            if tmp[i] != tmp[i-1]:
                ans.append(words[i])
        
        return ans
        