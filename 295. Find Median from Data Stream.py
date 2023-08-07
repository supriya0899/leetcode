class MedianFinder:

    def __init__(self):
        self.arr = []
        

    def addNum(self, num: int) -> None:
        self.arr.append(num)
        

    def findMedian(self) -> float:
        self.arr.sort()
        l , r = 0, len(self.arr)
        mid= (l+r)//2
        
        if len(self.arr) %2 == 0:
            a = self.arr[mid-1]
            b = self.arr[mid]
            return (a+b)/2
            
        else:
            return self.arr[mid]

        


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
