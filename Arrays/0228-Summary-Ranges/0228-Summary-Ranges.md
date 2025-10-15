# 228. Summary Ranges

## Problem Description

You are given a **sorted unique** integer array `nums`.

A **range** $[a,b]$ is the set of all integers from $a$ to $b$ (inclusive).

Return the **smallest sorted** list of ranges that **cover all the numbers in the array exactly**. That is, each element of `nums` is covered by exactly one of the ranges, and there is no integer $x$ such that $x$ is in one of the ranges but not in `nums`.

Each range $[a,b]$ in the list should be output as:

- `"a->b"` if $a \neq b$
- `"a"` if $a = b$

### Examples

#### Example 1:
**Input:** `nums = [0,1,2,4,5,7]`
**Output:** `["0->2","4->5","7"]`
**Explanation:** The ranges are:
- $[0,2] \to \text{"0->2"}$
- $[4,5] \to \text{"4->5"}$
- $[7,7] \to \text{"7"}$

#### Example 2:
**Input:** `nums = [0,2,3,4,6,8,9]`
**Output:** `["0","2->4","6","8->9"]`
**Explanation:** The ranges are:
- $[0,0] \to \text{"0"}$
- $[2,4] \to \text{"2->4"}$
- $[6,6] \to \text{"6"}$
- $[8,9] \to \text{"8->9"}$

### Constraints:
- $0 \le \text{nums.length} \le 20$
- $-2^{31} \le \text{nums}[i] \le 2^{31} - 1$
- All the values of `nums` are **unique**.
- `nums` is **sorted** in ascending order.
