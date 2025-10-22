# 4. Median of Two Sorted Arrays

## Problem Description

Given two sorted arrays `nums1` and `nums2` of size $m$ and $n$ respectively, return the **median** of the two sorted arrays.

The overall run time complexity should be $\mathbf{O(\log(\min(m, n)))}$ or $\mathbf{O(\log(m+n))}$.

### Examples

#### Example 1:
**Input:** `nums1 = [1,3], nums2 = [2]`
**Output:** `2.00000`
**Explanation:** Merged array = `[1,2,3]` and median is 2.

#### Example 2:
**Input:** `nums1 = [1,2], nums2 = [3,4]`
**Output:** `2.50000`
**Explanation:** Merged array = `[1,2,3,4]` and median is $(2 + 3) / 2 = 2.5$.

### Constraints:
- $\text{nums1.length} == m$
- $\text{nums2.length} == n$
- $0 \le m \le 1000$
- $0 \le n \le 1000$
- $1 \le m + n \le 2000$
- $-10^6 \le \text{nums1}[i], \text{nums2}[i] \le 10^6$
