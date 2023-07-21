class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:

        intervals = sorted(intervals, key = lambda x:x[0])

        count = 0

        lastEnd = [intervals[0][0], intervals[0][1]]

        for i in range(1, len(intervals)):
            #find non-overlapping intervals

            if intervals[i][0] >= lastEnd[1]:
                lastEnd[1] = intervals[i][1]
            else:
                #we found overlapping interval
                count +=1
                lastEnd[1] = min(lastEnd[1], intervals[i][1])
        return count



        
