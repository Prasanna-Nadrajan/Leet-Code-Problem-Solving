# 2221. Find Triangular Sum of an Array

## Problem Description

You are given a **0-indexed** integer array `nums`, where `nums[i]` is a digit between 0 and 9 (inclusive).

The **triangular sum** of `nums` is the value of the only element present in `nums` after the following process terminates:

1.  Let `nums` comprise of $n$ elements. If $n == 1$, **end** the process.
2.  Otherwise, **create** a new **0-indexed** integer array `newNums` of length $n - 1$.
3.  For each index $i$, where $0 \le i < n - 1$, **assign** the value of `newNums[i]` as $(\text{nums}[i] + \text{nums}[i+1]) \pmod{10}$, where $\%$ denotes the modulo operator.
4.  **Replace** the array `nums` with `newNums`.
5.  **Repeat** the entire process starting from step 1.

Return the triangular sum of `nums`.

### Examples

#### Example 1:
**Input:** `nums = [1,2,3,4,5]`
**Output:** `8`
**Explanation:**
The process is:
[1, 2, 3, 4, 5]
[3, 5, 7, 9] (i.e., (1+2)%10, (2+3)%10, ...)
[8, 2, 6]
[0, 8]
[8]

#### Example 2:
**Input:** `nums = [5]`
**Output:** `5`
**Explanation:** Since there is only one element in nums, the triangular sum is the value of that element itself.

### Constraints:
- $1 \le \text{nums.length} \le 1000$
- $0 \le \text{nums}[i] \le 9$
