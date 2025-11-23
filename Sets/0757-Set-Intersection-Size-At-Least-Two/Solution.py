from typing import List

class Solution:
    def intersectionSizeTwo(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: (x[1], -x[0]))
        chosen = []
        for start, end in intervals:
            count = 0
            for num in reversed(chosen):
                if num >= start and num <= end:
                    count += 1
                if count == 2:
                    break
            while count < 2:
                new_num = end - (1 - count)
                chosen.append(new_num)
                count += 1
        
        return len(chosen)
