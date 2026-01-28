# 383. Ransom Note (Easy)

You are given two strings, `ransomNote` and `magazine`. Your task is to determine whether `ransomNote` can be constructed using the letters available in `magazine`.

Each character in `magazine` can be used **at most once** when forming the `ransomNote`. This means that if a letter appears fewer times in `magazine` than required in `ransomNote`, construction is not possible.

Return `true` if `ransomNote` can be constructed using `magazine`, otherwise return `false`.

### Examples

* **Input:** ransomNote = "a", magazine = "b"
  **Output:** false

* **Input:** ransomNote = "aa", magazine = "ab"
  **Output:** false

* **Input:** ransomNote = "aa", magazine = "aab"
  **Output:** true

### Constraints

* 1 <= ransomNote.length, magazine.length <= 10⁵
* Both strings consist only of lowercase English letters
