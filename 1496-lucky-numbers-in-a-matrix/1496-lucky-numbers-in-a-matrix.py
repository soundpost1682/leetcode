class Solution:
    def luckyNumbers (self, matrix: List[List[int]]) -> List[int]:
        tmp = set(map(max, zip(*matrix)))
        for r in matrix:
            _min_ = min(r)
            if _min_ in tmp: return [_min_]
        return []
        
