# 1018. Binary Prefix Divisible By 5

## Problem Description

You are given a binary array `nums` (0-indexed).

We define $x_i$ as the number whose binary representation is the subarray $\text{nums}[0..i]$ (from most-significant-bit to least-significant-bit).

For example, if $\text{nums} = [1,0,1]$, then $x_0 = 1$, $x_1 = 2$, and $x_2 = 5$.

Return an array of booleans `answer` where $\text{answer}[i]$ is **true** if $x_i$ is divisible by 5.

### Examples

#### Example 1:
**Input:** $\text{nums} = [0,1,1]$
**Output:** $[\text{true},\text{false},\text{false}]$
**Explanation:** The input numbers in binary are 0, 01, 011; which are 0, 1, and 3 in base-10.
Only the first number (0) is divisible by 5, so $\text{answer}[0]$ is true.

#### Example 2:
**Input:** $\text{nums} = [1,1,1]$
**Output:** $[\text{false},\text{false},\text{false}]$

### Constraints:
- $1 \le \text{nums.length} \le 10^5$
- $\text{nums}[i]$ is either 0 or 1.
