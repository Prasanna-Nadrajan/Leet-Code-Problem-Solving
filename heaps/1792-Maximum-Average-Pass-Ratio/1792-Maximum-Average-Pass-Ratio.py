import heapq

class Solution:
    def maxAverageRatio(self, classes, extraStudents):
        def gain(a, b):
            return (a + 1) / (b + 1) - a / b
        heap = [(-gain(a, b), a, b) for a, b in classes]
        heapq.heapify(heap)

        for _ in range(extraStudents):
            g, a, b = heapq.heappop(heap)
            a += 1
            b += 1
            heapq.heappush(heap, (-gain(a, b), a, b))

        return sum(a / b for _, a, b in heap) / len(classes)
