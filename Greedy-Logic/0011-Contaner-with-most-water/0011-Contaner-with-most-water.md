# 11. Container With Most Water

## Problem Description

You are given an integer array `height` of length $n$. There are $n$ vertical lines drawn such that the two endpoints of the $i^{th}$ line are $(i, 0)$ and $(i, \text{height}[i])$.

Find two lines that together with the x-axis form a container, such that the container contains the most water.

Return the **maximum amount of water** a container can store.

**Notice** that you may not slant the container.

### Examples

#### Example 1:
**Input:** `height = [1,8,6,2,5,4,8,3,7]`
**Output:** `49`
**Explanation:** The vertical lines are represented by the array. The maximum area of water the container can hold is 49 (formed by the lines of height 8 and 7, which have a width of 7).

#### Example 2:
**Input:** `height = [1,1]`
**Output:** `1`

### Constraints:
- $n == \text{height.length}$
- $2 \le n \le 10^5$
- $0 \le \text{height}[i] \le 10^4$
