# 2300. Successful Pairs of Spells and Potions

You are given two positive integer arrays:

* `spells` of length `n`, where `spells[i]` represents the strength of the *i-th* spell
* `potions` of length `m`, where `potions[j]` represents the strength of the *j-th* potion

You are also given an integer `success`.

A **spell and potion pair** is considered *successful* if:

```
spells[i] * potions[j] >= success
```

For each spell, determine how many potions can form a successful pair with it.

Return an integer array `pairs` of length `n`, where `pairs[i]` is the number of successful pairs for the `i-th` spell.

---

## Examples

**Example 1**

Input:

```
spells = [5,1,3]
potions = [1,2,3,4,5]
success = 7
```

Output:

```
[4,0,3]
```

**Example 2**

Input:

```
spells = [3,1,2]
potions = [8,5,8]
success = 16
```

Output:

```
[2,0,2]
```

---

## Constraints

* `n == spells.length`
* `m == potions.length`
* `1 <= n, m <= 10^5`
* `1 <= spells[i], potions[i] <= 10^5`
* `1 <= success <= 10^10`
