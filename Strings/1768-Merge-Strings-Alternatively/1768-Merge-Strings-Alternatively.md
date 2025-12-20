# 1768. Merge Strings Alternately

## Problem Statement

You are given two strings `word1` and `word2`. Merge the strings by adding letters in **alternating order**, starting with `word1`.

If one string is longer than the other, append the remaining letters of the longer string to the end of the merged result.

Return the final merged string.

---

## Examples

### Example 1

**Input:**

```
word1 = "abc", word2 = "pqr"
```

**Output:**

```
"apbqcr"
```

---

### Example 2

**Input:**

```
word1 = "ab", word2 = "pqrs"
```

**Output:**

```
"apbqrs"
```

---

### Example 3

**Input:**

```
word1 = "abcd", word2 = "pq"
```

**Output:**

```
"apbqcd"
```

---

## Constraints

* `1 <= word1.length, word2.length <= 100`
* Both strings consist of lowercase English letters
