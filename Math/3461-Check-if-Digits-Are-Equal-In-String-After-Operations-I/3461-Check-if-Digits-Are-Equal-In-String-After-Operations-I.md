# 3461. Check If Digits Are Equal in String After Operations I

## Problem Description

You are given a string `s` consisting of digits. Perform the following operation repeatedly until the string has **exactly** two digits:

1.  Let `s` comprise of $n$ elements. If $n == 2$, **end** the process.
2.  For each pair of consecutive digits in `s`, starting from the first digit, calculate a new digit as the sum of the two digits **modulo 10**.
3.  **Replace** `s` with the sequence of newly calculated digits, **maintaining the order** in which they are computed.
4.  **Repeat** the entire process starting from step 1.

Return **true** if the final two digits in `s` are the **same**; otherwise, return **false**.

### Examples

#### Example 1:
**Input:** `s = "3902"`
**Output:** `true`
**Explanation:**
1.  Initially, $s = \text{"3902"}$.
2.  First operation: $(3+9)\%10=2$, $(9+0)\%10=9$, $(0+2)\%10=2$. $s$ becomes $\text{"292"}$.
3.  Second operation: $(2+9)\%10=1$, $(9+2)\%10=1$. $s$ becomes $\text{"11"}$.
Since the digits in $\text{"11"}$ are the same, the output is $\text{true}$.

#### Example 2:
**Input:** $s = \text{"34789"}$
**Output:** $\text{false}$
**Explanation:**
1.  Initially, $s = \text{"34789"}$.
2.  After the first operation, $s = \text{"7157"}$.
3.  After the second operation, $s = \text{"862"}$.
4.  After the third operation, $s = \text{"48"}$.
Since $\text{'4'} \neq \text{'8'}$, the output is $\text{false}$.

### Constraints:
- $3 \le \text{s.length} \le 100$
- $s$ consists of only digits.
