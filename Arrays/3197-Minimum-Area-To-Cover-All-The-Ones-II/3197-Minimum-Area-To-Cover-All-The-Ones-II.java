from typing import List

class Solution:
    def min_area(self, cells):
        """Return area of bounding box covering given cells."""
        if not cells:
            return 0
        rows = [r for r, c in cells]
        cols = [c for r, c in cells]
        return (max(rows) - min(rows) + 1) * (max(cols) - min(cols) + 1)

    def minimumSum(self, grid: List[List[int]]) -> int:
        R, C = len(grid), len(grid[0])
        ones = [(r, c) for r in range(R) for c in range(C) if grid[r][c] == 1]
        if not ones:
            return 0

        ans = float("inf")

        # ----- Case 1: vertical 3-split -----
        for c1 in range(1, C - 1):
            for c2 in range(c1 + 1, C):
                rect1 = [(r, c) for r, c in ones if c < c1]
                rect2 = [(r, c) for r, c in ones if c1 <= c < c2]
                rect3 = [(r, c) for r, c in ones if c >= c2]
                if rect1 and rect2 and rect3:
                    ans = min(ans, self.min_area(rect1) + self.min_area(rect2) + self.min_area(rect3))

        # ----- Case 2: horizontal 3-split -----
        for r1 in range(1, R - 1):
            for r2 in range(r1 + 1, R):
                rect1 = [(r, c) for r, c in ones if r < r1]
                rect2 = [(r, c) for r, c in ones if r1 <= r < r2]
                rect3 = [(r, c) for r, c in ones if r >= r2]
                if rect1 and rect2 and rect3:
                    ans = min(ans, self.min_area(rect1) + self.min_area(rect2) + self.min_area(rect3))

        # ----- Case 3: vertical + horizontal (L shape partitions) -----
        for c in range(1, C):
            for r in range(1, R):
                rect1 = [(x, y) for x, y in ones if y < c]   # left side
                rect2 = [(x, y) for x, y in ones if y >= c and x < r]  # top-right
                rect3 = [(x, y) for x, y in ones if y >= c and x >= r] # bottom-right
                if rect1 and rect2 and rect3:
                    ans = min(ans, self.min_area(rect1) + self.min_area(rect2) + self.min_area(rect3))

                rect1 = [(x, y) for x, y in ones if y >= c]  # right side
                rect2 = [(x, y) for x, y in ones if y < c and x < r]   # top-left
                rect3 = [(x, y) for x, y in ones if y < c and x >= r]  # bottom-left
                if rect1 and rect2 and rect3:
                    ans = min(ans, self.min_area(rect1) + self.min_area(rect2) + self.min_area(rect3))

        # ----- Case 4: horizontal + vertical (symmetric of Case 3) -----
        for r in range(1, R):
            for c in range(1, C):
                rect1 = [(x, y) for x, y in ones if x < r]   # top side
                rect2 = [(x, y) for x, y in ones if x >= r and y < c]  # bottom-left
                rect3 = [(x, y) for x, y in ones if x >= r and y >= c] # bottom-right
                if rect1 and rect2 and rect3:
                    ans = min(ans, self.min_area(rect1) + self.min_area(rect2) + self.min_area(rect3))

                rect1 = [(x, y) for x, y in ones if x >= r]  # bottom side
                rect2 = [(x, y) for x, y in ones if x < r and y < c]   # top-left
                rect3 = [(x, y) for x, y in ones if x < r and y >= c]  # top-right
                if rect1 and rect2 and rect3:
                    ans = min(ans, self.min_area(rect1) + self.min_area(rect2) + self.min_area(rect3))

        return ans if ans != float("inf") else -1
