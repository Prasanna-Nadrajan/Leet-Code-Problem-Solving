# 287. Find the Duplicate Number

## Problem Description

Given an array of integers `nums` containing $n + 1$ integers where each integer is in the range $[1, n]$ inclusive.

There is only **one repeated number** in `nums`, return **this repeated number**.

You must solve the problem **without modifying the array** `nums` and using only **constant extra space**.

### Examples

#### Example 1:
**Input:** `nums = [1,3,4,2,2]`
**Output:** `2`

#### Example 2:
**Input:** `nums = [3,1,3,4,2]`
**Output:** `3`

#### Example 3:
**Input:** `nums = [3,3,3,3,3]`
**Output:** `3`

### Constraints:
- $1 \le n \le 10^5$
- $\text{nums.length} == n + 1$
- $1 \le \text{nums}[i] \le n$
- All the integers in `nums` appear only once except for **precisely one integer** which appears **two or more** times.
