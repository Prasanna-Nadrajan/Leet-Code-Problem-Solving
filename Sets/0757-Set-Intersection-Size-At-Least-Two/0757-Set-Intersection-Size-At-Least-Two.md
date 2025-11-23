# 757. Set Intersection Size At Least Two

## Problem Description

You are given a 2D integer array `intervals` where $\text{intervals}[i] = [start_i, end_i]$ represents all the integers from $start_i$ to $end_i$ inclusively.

A **containing set** is an array `nums` where each interval from `intervals` has **at least two** integers in `nums`.

For example, if $\text{intervals} = [[1,3], [3,7], [8,9]]$, then $[1,2,4,7,8,9]$ and $[2,3,4,8,9]$ are containing sets.

Return the **minimum possible size** of a containing set.

### Examples

#### Example 1:
**Input:** $\text{intervals} = [[1,3],[3,7],[8,9]]$
**Output:** $5$
**Explanation:** Let $\text{nums} = [2, 3, 4, 8, 9]$. It can be shown that there cannot be any containing array of size 4.

#### Example 2:
**Input:** $\text{intervals} = [[1,3],[1,4],[2,5],[3,5]]$
**Output:** $3$
**Explanation:** Let $\text{nums} = [2, 3, 4]$. It can be shown that there cannot be any containing array of size 2.

#### Example 3:
**Input:** $\text{intervals} = [[1,2],[2,3],[2,4],[4,5]]$
**Output:** $5$
**Explanation:** Let $\text{nums} = [1, 2, 3, 4, 5]$. It can be shown that there cannot be any containing array of size 4.

### Constraints:
- $1 \le \text{intervals.length} \le 3000$
- $\text{intervals}[i].\text{length} == 2$
- $0 \le \text{start}_i < \text{end}_i \le 10^8$
