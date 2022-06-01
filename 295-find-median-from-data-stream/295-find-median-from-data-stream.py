class MedianFinder:
    def __init__(self):
        self.heaps = [], []

    def addNum(self, num):
        small, large = self.heaps
        heappush(small, -heappushpop(large, num))
        if len(large) < len(small):
            heappush(large, -heappop(small))

    def findMedian(self):
        small, large = self.heaps
        if len(large) > len(small):
            return float(large[0])
        return (large[0] - small[0]) / 2.0
    
    
    
#     def __init__(self):
#         self.nums = []

#     def addNum(self, num: int) -> None:
#         self.nums.append(num)

#     def findMedian(self) -> float:
#         n = len(self.nums)
#         self.nums.sort()
#         if n % 2 != 0 :
#             return self.nums[n//2]
#         else:
#             return (self.nums[n//2] + self.nums[(n//2)-1])/2 
             


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()