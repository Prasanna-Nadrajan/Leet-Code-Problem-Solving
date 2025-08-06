class SegmentTree:
    
    def __init__(self, arr):
        self.n = len(arr)
        self.tree = [0] * (4 * self.n)
        self.arr = arr
        self.build(1, 0, self.n - 1)

    def build(self, node, start, end):
        if start == end:
            self.tree[node] = self.arr[start]
            return
        mid = (start + end) // 2
        self.build(2 * node, start, mid)
        self.build(2 * node + 1, mid + 1, end)
        self.tree[node] = max(self.tree[2 * node], self.tree[2 * node + 1])

    def query_and_update(self, node, start, end, fruit_size):
        if self.tree[node] < fruit_size:
            return -1

        if start == end:
            self.tree[node] = 0
            return start

        mid = (start + end) // 2
        result = -1

        if self.tree[2 * node] >= fruit_size:
            result = self.query_and_update(2 * node, start, mid, fruit_size)
        
        if result == -1 and self.tree[2 * node + 1] >= fruit_size:
            result = self.query_and_update(2 * node + 1, mid + 1, end, fruit_size)

        self.tree[node] = max(self.tree[2 * node], self.tree[2 * node + 1])
        return result


class Solution:
    def numOfUnplacedFruits(self, fruits: list[int], baskets: list[int]) -> int:
        n = len(fruits)
        segment_tree = SegmentTree(baskets)
        unplaced_count = 0

        for fruit_size in fruits:
            basket_index = segment_tree.query_and_update(1, 0, n - 1, fruit_size)
            
            if basket_index == -1:
                unplaced_count += 1
        
        return unplaced_count
