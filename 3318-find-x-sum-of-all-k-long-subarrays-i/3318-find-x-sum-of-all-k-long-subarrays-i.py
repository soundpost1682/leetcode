class Solution:
    def findXSum(self, nums: List[int], k: int, x: int) -> List[int]:
        tmp,ans = len(nums), []

        for i in range(tmp - k+1):
            win = nums[i:i+k]
            fre = Counter(win)
            sort_fre = sorted(fre.items(), key=lambda a: (-a[1], -a[0]))
            top = set(n for n, _ in sort_fre[:x])
            xsum = sum(n for n in win if n in top)
            ans.append(xsum)
        return ans

        