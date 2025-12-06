3578. Count Partitions With Max-Min Difference at Most K

Problem Description

You are given an integer array nums and an integer $k$. Your task is to partition nums into one or more non-empty contiguous segments such that in each segment, the difference between its maximum and minimum elements is at most $k$.

Return the total number of ways to partition nums under this condition.

Since the answer may be too large, return it modulo $10^9 + 7$.

Examples

Example 1:

Input: $\text{nums} = [9,4,1,3,7], k = 4$
Output: $6$
Explanation:
There are 6 valid partitions where the difference between the maximum and minimum elements in each segment is at most $k = 4$:

$[[9], [4], [1], [3], [7]]$

$[[9], [4], [1], [3, 7]]$

$[[9], [4], [1, 3], [7]]$

$[[9], [4, 1], [3], [7]]$

$[[9], [4, 1], [3, 7]]$

$[[9], [4, 1, 3], [7]]$

Example 2:

Input: $\text{nums} = [3,3,4], k = 0$
Output: $2$
Explanation:
There are 2 valid partitions that satisfy the given conditions:

$[[3], [3], [4]]$

$[[3, 3], [4]]$

Constraints:

$2 \le \text{nums.length} \le 5 \times 10^4$

$1 \le \text{nums}[i] \le 10^9$

$0 \le k \le 10^9$
