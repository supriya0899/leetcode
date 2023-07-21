class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:

        intervals = sorted(intervals, key = lambda x:x[0])

        ans = []
        
        lastEnd = [intervals[0][0], intervals[0][1]]

        for i in range(1, len(intervals)):
            if intervals[i][0] <= lastEnd[1]:
                lastEnd[1] = max(lastEnd[1], intervals[i][1])
            else:
                ans.append(lastEnd)
                lastEnd = [intervals[i][0], intervals[i][1]]
        ans.append(lastEnd)
        return ans

