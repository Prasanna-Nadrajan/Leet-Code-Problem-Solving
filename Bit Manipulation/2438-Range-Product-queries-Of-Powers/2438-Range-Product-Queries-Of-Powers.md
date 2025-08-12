# Range Product Queries of Powers

## Problem
Given a positive integer `n`, there exists a **0-indexed array** called `powers`, composed of the minimum number of powers of 2 that sum to `n`.  
The array is sorted in **non-decreasing order**, and there is **only one way** to form the array.

You are also given a **0-indexed 2D integer array** `queries`, where `queries[i] = [left_i, right_i]`.  
Each query asks for the **product** of all `powers[j]` where `left_i <= j <= right_i`.

Return an array `answers`, where `answers[i]` is the answer to the `i`-th query **modulo** `10^9 + 7`.

---

## Example 1

**Input:**
n = 15
queries = [[0,1],[2,2],[0,3]]

makefile
Copy
Edit

**Output:**
[2, 4, 64]

**Explanation:**
- For `n = 15`, the `powers` array is `[1, 2, 4, 8]`.
- Query 1: `powers[0] * powers[1] = 1 * 2 = 2`
- Query 2: `powers[2] = 4`
- Query 3: `powers[0] * powers[1] * powers[2] * powers[3] = 1 * 2 * 4 * 8 = 64`

---

## Example 2

**Input:**
n = 2
queries = [[0,0]]


**Output:**
[2]


**Explanation:**
- For `n = 2`, `powers = [2]`.
- The only query result is `powers[0] = 2`.

---

## Constraints
- `1 <= n <= 10^9`
- `1 <= queries.length <= 10^5`
- `0 <= start_i <= end_i < powers.length`
