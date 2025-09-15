# 🧠 Problem Statement

**Leetcode #1935 — Easy**

You are given:
- A string `text` consisting of words separated by a single space  
- A string `brokenLetters` containing distinct lowercase letters representing broken keys on a keyboard

🎯 **Goal**:  
Return the number of words in `text` that can be **fully typed** using the working keys.

> A word is considered typable if **none of its letters** are in `brokenLetters`.

---

## 📊 Examples

### Example 1  
**Input:** `text = "hello world"`, `brokenLetters = "ad"`  
**Output:** `1`  
**Explanation:** "world" contains 'd' → cannot be typed

---

### Example 2  
**Input:** `text = "leet code"`, `brokenLetters = "lt"`  
**Output:** `1`  
**Explanation:** "leet" contains 'l' and 't' → cannot be typed

---

### Example 3  
**Input:** `text = "leet code"`, `brokenLetters = "e"`  
**Output:** `0`  
**Explanation:** Both words contain 'e' → neither can be typed

---

## 📌 Constraints

- `1 <= text.length <= 10⁴`  
- `0 <= brokenLetters.length <= 26`  
- `text` contains words separated by a single space  
- No leading or trailing spaces  
- All characters are lowercase English letters  
- `brokenLetters` contains distinct characters

---

## 💡 Tags

`String` `Set` `Filtering` `Simulation`
