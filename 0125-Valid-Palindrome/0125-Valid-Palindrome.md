# 125. Valid Palindrome

## Problem Statement

A phrase is considered a **palindrome** if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward.

Alphanumeric characters include **letters and numbers**.

Given a string `s`, return `true` if it is a palindrome, or `false` otherwise.

---

## Examples

### Example 1

**Input:**

```
s = "A man, a plan, a canal: Panama"
```

**Output:**

```
true
```

**Explanation:**
After cleaning and normalizing the string:

```
"amanaplanacanalpanama"
```

which is a palindrome.

---

### Example 2

**Input:**

```
s = "race a car"
```

**Output:**

```
false
```

**Explanation:**
After cleaning:

```
"raceacar"
```

which is not a palindrome.

---

### Example 3

**Input:**

```
s = " "
```

**Output:**

```
true
```

**Explanation:**
After removing non-alphanumeric characters, the string becomes empty. An empty string is considered a palindrome.

---

## Constraints

* `1 <= s.length <= 2 * 10^5`
* `s` consists only of printable ASCII characters
