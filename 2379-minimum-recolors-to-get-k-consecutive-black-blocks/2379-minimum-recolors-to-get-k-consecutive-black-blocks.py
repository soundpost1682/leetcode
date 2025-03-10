class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        tmp = len(blocks)
        tmp2 = blocks[:k].count('W')
        answer = tmp2
        for i in range(k, tmp):
            if blocks[i] == 'W':
                tmp2 +=1
            if blocks[i-k] == 'W':
                tmp2 -=1
            answer = min(answer, tmp2)
        return answer
        