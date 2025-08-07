# 🌀 Zigzag Conversion

## Problem Statement

The string `"PAYPALISHIRING"` is written in a zigzag pattern on a given number of rows like this (when `numRows = 3`):

```
P   A   H   N  
A P L S I I G  
Y   I   R
```

Then the result is formed by reading line by line: `"PAHNAPLSIIGYIR"`.

Write a function that takes a string and a number of rows and returns the string after converting it to the zigzag pattern.

---

## Function Signature

```python
def convert(s: str, numRows: int) -> str
```

---

## Examples

### Example 1:
- **Input:** `s = "PAYPALISHIRING", numRows = 3`
- **Output:** `"PAHNAPLSIIGYIR"`

### Example 2:
- **Input:** `s = "PAYPALISHIRING", numRows = 4`
- **Output:** `"PINALSIGYAHRPI"`

Zigzag structure for 4 rows:

```
P     I    N  
A   L S  I G  
Y A   H R  
P     I
```

### Example 3:
- **Input:** `s = "A", numRows = 1`
- **Output:** `"A"`

---

## Constraints

- `1 <= s.length <= 1000`
- `s` consists of English letters (lower-case and upper-case), commas `,`, and periods `.`.
- `1 <= numRows <= 1000`
```
