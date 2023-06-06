import heapq


## Runtime 87.8%
## Memory 80.1%
class SmallestInfiniteSet:

    def __init__(self):
        self.num = 1
        self.res = []

    def popSmallest(self) -> int:
        if self.res:
            return heapq.heappop(self.res)
        self.num += 1
        return self.num - 1

    def addBack(self, num: int) -> None:
        if self.num > num and num not in self.res:
            heapq.heappush(self.res, num)


# Your SmallestInfiniteSet object will be instantiated and called as such:
# obj = SmallestInfiniteSet()
# param_1 = obj.popSmallest()
# obj.addBack(num)