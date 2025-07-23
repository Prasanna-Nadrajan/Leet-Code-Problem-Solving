# Maximum Points from Removing Substrings

You are given a string `s` and two integers `x` and `y`.  
You can perform **two types of operations** any number of times:

- Remove the substring `"ab"` and **gain `x` points**.  
  Example: Removing `"ab"` from `"cabxbae"` becomes `"cxbae"`.

- Remove the substring `"ba"` and **gain `y` points**.  
  Example: Removing `"ba"` from `"cabxbae"` becomes `"cabxe"`.

---

### Goal:
Return the **maximum points** you can gain after applying the above operations on `s`.

---

### Examples

#### Example 1:
**Input:**  
`s = "cdbcbbaaabab", x = 4, y = 5`  
**Output:**  
`19`

**Explanation:**  
- Remove `"ba"` from `"cdbcbbaaabab"` → `"cdbcbbaaab"` → +5  
- Remove `"ab"` from `"cdbcbbaaab"` → `"cdbcbbaa"` → +4  
- Remove `"ba"` from `"cdbcbbaa"` → `"cdbcba"` → +5  
- Remove `"ba"` from `"cdbcba"` → `"cdbc"` → +5  
**Total = 5 + 4 + 5 + 5 = 19**

---

#### Example 2:
**Input:**  
`s = "aabbaaxybbaabb", x = 5, y = 4`  
**Output:**  
`20`

---

### Constraints:

- `1 <= s.length <= 10⁵`  
- `1 <= x, y <= 10⁴`  
- `s` consists of lowercase English letters.
