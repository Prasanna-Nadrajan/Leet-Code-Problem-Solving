### Problem: Roman to Integer

Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.

| Symbol | Value |
|--------|-------|
| I      | 1     |
| V      | 5     |
| X      | 10    |
| L      | 50    |
| C      | 100   |
| D      | 500   |
| M      | 1000  |

Roman numerals are usually written from largest to smallest left to right. But some numbers use subtraction rules:
- I before V (5) and X (10) → 4, 9
- X before L (50) and C (100) → 40, 90
- C before D (500) and M (1000) → 400, 900

Given a Roman numeral string `s`, convert it to an integer.

#### Examples:

**Example 1**  
Input: s = "III"  
Output: 3

**Example 2**  
Input: s = "LVIII"  
Output: 58  
Explanation: L = 50, V = 5, III = 3

**Example 3**  
Input: s = "MCMXCIV"  
Output: 1994  
Explanation: M = 1000, CM = 900, XC = 90, IV = 4

#### Constraints:
- 1 <= s.length <= 15
- `s` contains only characters I, V, X, L, C, D, M
- It is guaranteed that `s` is a valid Roman numeral in the range [1, 3999]
