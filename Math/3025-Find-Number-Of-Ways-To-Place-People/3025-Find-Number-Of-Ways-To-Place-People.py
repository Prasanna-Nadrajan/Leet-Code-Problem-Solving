class Solution(object):
    def numberOfPairs(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        count = 0
        n = len(points)
        for i in range(n):
            for j in range(n):
                if i == j:
                    continue

                x_A, y_A = points[i]
                x_B, y_B = points[j]

                if x_A <= x_B and y_A >= y_B:
                    
                    is_empty_rectangle = True
                    for k in range(n):
                        if k == i or k == j:
                            continue

                        x_C, y_C = points[k]

                        if x_A <= x_C <= x_B and y_B <= y_C <= y_A:
                            is_empty_rectangle = False
                            break 

                    if is_empty_rectangle:
                        count += 1
                        
        return count
