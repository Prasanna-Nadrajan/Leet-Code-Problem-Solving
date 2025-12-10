3577. Count the Number of Computer Unlocking Permutations

Problem Description

You are given an array complexity of length $n$.

There are $n$ locked computers in a room with labels from 0 to $n - 1$, each with its own unique password. The password of the computer $i$ has a complexity $\text{complexity}[i]$.

The password for the computer labeled 0 is already decrypted and serves as the root. All other computers must be unlocked using it or another previously unlocked computer, following this information:

You can decrypt the password for the computer $i$ using the password for computer $j$, where $j$ is any integer less than $i$ with a lower complexity. (i.e. $j < i$ and $\text{complexity}[j] < \text{complexity}[i]$)

To decrypt the password for computer $i$, you must have already unlocked a computer $j$ such that $j < i$ and $\text{complexity}[j] < \text{complexity}[i]$.

Find the number of permutations of $[0, 1, 2, \dots, (n - 1)]$ that represent a valid order in which the computers can be unlocked, starting from computer 0 as the only initially unlocked one.

Since the answer may be large, return it modulo $10^9 + 7$.

Note: The password for the computer with label 0 is decrypted, and not the computer with the first position in the permutation.

Examples

Example 1:

Input: $\text{complexity} = [1,2,3]$
Output: $2$
Explanation: The valid permutations are:

$[0, 1, 2]$: Unlock 0. Unlock 1 with 0 (since $\text{complexity}[0] < \text{complexity}[1]$). Unlock 2 with 1 (since $\text{complexity}[1] < \text{complexity}[2]$).

$[0, 2, 1]$: Unlock 0. Unlock 2 with 0 (since $\text{complexity}[0] < \text{complexity}[2]$). Unlock 1 with 0 (since $\text{complexity}[0] < \text{complexity}[1]$).

Example 2:

Input: $\text{complexity} = [3,3,3,4,4,4]$
Output: $0$
Explanation: There are no possible permutations which can unlock all computers.

Constraints:

$2 \le \text{complexity.length} \le 10^5$

$1 \le \text{complexity}[i] \le 10^9$
