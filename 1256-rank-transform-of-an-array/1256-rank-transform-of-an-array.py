class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        tmp={v:i +1 for i, v in enumerate(sorted(set(arr)))}
        return [tmp[ans] for ans in arr]

