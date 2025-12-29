# 2390. Removing Stars From a String

## Problem Statement

You are given a string `s` that contains lowercase English letters and stars (`*`).

In one operation, you can:

* Choose a star (`*`) in the string.
* Remove the closest non-star character to its **left**, and also remove the star itself.

After performing all possible operations, return the final resulting string.

The problem guarantees that:

* The operation is always possible.
* The resulting string is unique.

---

## Examples

**Example 1:**

Input: `s = "leet**cod*e"`

Output: `"lecoe"`

Explanation:
Characters to the left of each star are removed step by step along with the star itself.

**Example 2:**

Input: `s = "erase*****"`

Output: `""`

Explanation:
All characters are removed after processing every star.

---

## Constraints

* `1 <= s.length <= 10^5`
* `s` consists of lowercase English letters and `*`
* The operation can always be performed
