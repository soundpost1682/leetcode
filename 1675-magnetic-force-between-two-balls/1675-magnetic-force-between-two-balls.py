class Solution:
    def maxDistance(self, position: List[int], m: int) -> int:
        position.sort()
        def cnt(dic):
            a=1
            b=position[0]
            for i in position:
                if i - b > dic:
                    b = i
                    a += 1
            return a
        return bisect_left(range(position[-1] - position[0]), True, key=lambda dic:cnt(dic) < m)



