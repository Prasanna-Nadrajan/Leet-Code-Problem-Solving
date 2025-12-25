# 1679. Max Number of K-Sum Pairs

## Problem Statement

You are given an integer array `nums` and an integer `k`.

In one operation, you can pick two numbers from the array whose sum equals `k` and remove them from the array.

Return the **maximum number of operations** you can perform on the array.

---

## Examples

**Example 1:**

Input: `nums = [1,2,3,4], k = 5`

Output: `2`

Explanation:

* Remove `1` and `4` → remaining `[2,3]`
* Remove `2` and `3` → remaining `[]`

**Example 2:**

Input: `nums = [3,1,3,4,3], k = 6`

Output: `1`

Explanation:

* Remove two `3`s → remaining `[1,4,3]`

---

## Constraints

* `1 <= nums.length <= 10^5`
* `1 <= nums[i] <= 10^9`
* `1 <= k <= 10^9`
