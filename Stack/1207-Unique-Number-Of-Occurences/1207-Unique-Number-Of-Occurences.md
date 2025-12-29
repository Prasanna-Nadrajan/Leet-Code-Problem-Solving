# 1207. Unique Number of Occurrences

## Problem Statement

You are given an integer array `arr`.

Your task is to determine whether the number of occurrences of **each distinct value** in the array is unique.

If no two values have the same frequency, return `true`. Otherwise, return `false`.

---

## Examples

**Example 1:**

Input: `arr = [1,2,2,1,1,3]`

Output: `true`

Explanation:

* `1` appears 3 times
* `2` appears 2 times
* `3` appears 1 time
  All occurrence counts are unique.

**Example 2:**

Input: `arr = [1,2]`

Output: `false`

Explanation:
Both values appear exactly once, so the occurrence counts are not unique.

---

## Constraints

* `1 <= arr.length <= 1000`
* `-1000 <= arr[i] <= 1000`
