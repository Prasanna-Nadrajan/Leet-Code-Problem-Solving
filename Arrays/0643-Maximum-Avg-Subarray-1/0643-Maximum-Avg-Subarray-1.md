# 643. Maximum Average Subarray I

## Problem Statement

You are given an integer array `nums` consisting of `n` elements, and an integer `k`.

Find a **contiguous subarray** of length `k` that has the **maximum average value** and return this value.

Any answer with an absolute error less than `10^-5` will be accepted.

---

## Examples

**Example 1:**

Input: `nums = [1,12,-5,-6,50,3], k = 4`

Output: `12.75000`

Explanation:
The subarray `[12, -5, -6, 50]` gives the maximum average:
`(12 - 5 - 6 + 50) / 4 = 12.75`

**Example 2:**

Input: `nums = [5], k = 1`

Output: `5.00000`

---

## Constraints

* `1 <= k <= n <= 10^5`
* `-10^4 <= nums[i] <= 10^4`
