class Solution:
    def intersectionSizeTwo(intervals: list[list[int]]) -> int:
        intervals.sort(key=lambda x : (x[1],-x[0]))
        m = 0 #count of number in set
        largest = second = -1
        for interval in intervals:
            start , end = interval[0],interval[1]
            if start<=second:
                continue
            elif start  > largest:
                m+=2
                second = end-1
                largest = end
            else:
                m+=1
                second = largest
                largest = end
        return m
        