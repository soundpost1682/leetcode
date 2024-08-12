class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.mheap=[]
        for number in nums:
            self.add(number)

    def add(self, val: int) -> int:
        if len(self.mheap) < self.k:
            heapq.heappush(self.mheap, val)
        elif val > self.mheap[0]:
            heapq.heapreplace(self.mheap, val)
        return self.mheap[0]
        
        


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)