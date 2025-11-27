# 3756. Concatenate Non-Zero Digits and Multiply by Sum II

## Problem Description

You are given a string `s` of length $m$ consisting of digits. You are also given a 2D integer array `queries`, where $\text{queries}[i] = [l_i, r_i]$.

For each $\text{queries}[i]$, extract the **substring** $\text{s}[l_i..r_i]$. Then, perform the following:
1. Form a new integer $x$ by concatenating all the **non-zero digits** from the substring in their original order. If there are no non-zero digits, $x = 0$.
2. Let $\text{sum}$ be the **sum of digits** in $x$.
3. The answer is $x \times \text{sum}$.

Return an array of integers $\text{answer}$ where $\text{answer}[i]$ is the answer to the $i^{th}$ query.

Since the answers may be very large, return them **modulo $10^9 + 7$**.

### Examples

#### Example 1:
**Input:** $\text{s} = \text{"10203004"}, \text{queries} = [[0,7],[1,3],[4,6]]$
**Output:** $[12340, 4, 9]$
**Explanation:**
- $\text{s}[0..7] = \text{"10203004"}$. $x = 1234$. $\text{sum} = 10$. Answer is $1234 \times 10 = 12340$.
- $\text{s}[1..3] = \text{"020"}$. $x = 2$. $\text{sum} = 2$. Answer is $2 \times 2 = 4$.
- $\text{s}[4..6] = \text{"300"}$. $x = 3$. $\text{sum} = 3$. Answer is $3 \times 3 = 9$.

#### Example 3:
**Input:** $\text{s} = \text{"9876543210"}, \text{queries} = [[0,9]]$
**Output:** $[444444137]$
**Explanation:**
$\text{s}[0..9] = \text{"9876543210"}$. $x = 987654321$. $\text{sum} = 45$.
Answer is $987654321 \times 45 = 44444444445$.
We return $44444444445 \pmod{10^9 + 7} = 444444137$.

### Constraints:
- $1 \le m == \text{s.length} \le 10^5$
- $1 \le \text{queries.length} \le 10^5$
- $0 \le l_i \le r_i < m$
