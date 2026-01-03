# 1411. Number of Ways to Paint N × 3 Grid

You have a grid of size `n × 3` and you want to paint each cell of the grid with exactly one of the three colors:

- Red  
- Yellow  
- Green  

while making sure that no two adjacent cells have the same color (i.e., no two cells that share vertical or horizontal sides have the same color).

Given `n`, the number of rows of the grid, return the number of ways you can paint this grid.

Since the answer may grow large, return the result modulo **10⁹ + 7**.

---

## Example 1

**Input:**
n = 1

makefile
Copy code

**Output:**
12

yaml
Copy code

**Explanation:**  
There are 12 possible ways to paint the grid.

---

## Example 2

**Input:**
n = 5000

makefile
Copy code

**Output:**
30228214

yaml
Copy code

---

## Constraints

- `n == grid.length`
- `1 <= n <= 5000`
