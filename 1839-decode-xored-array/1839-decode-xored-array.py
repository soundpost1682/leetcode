class Solution:
    def decode(self, encoded: List[int], first: int) -> List[int]:
        answer = [first]
        for i in encoded:
            answer.append(answer[-1] ^ i)
        return answer
