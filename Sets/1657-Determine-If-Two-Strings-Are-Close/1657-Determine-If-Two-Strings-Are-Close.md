1657. Determine if Two Strings Are Close

Difficulty: Medium

Problem Statement

Two strings are considered close if you can transform one string into the other using the following operations any number of times:

Operation 1:
Swap any two existing characters.
Example:
abcde → aecdb

Operation 2:
Transform every occurrence of one existing character into another existing character, and do the same with the other character.
Example:
aacabb → bbcbaa
(All 'a' characters turn into 'b', and all 'b' characters turn into 'a')

Given two strings word1 and word2, return true if they are close, otherwise return false.

Examples

Example 1
Input: word1 = "abc", word2 = "bca"
Output: true

Example 2
Input: word1 = "a", word2 = "aa"
Output: false

Example 3
Input: word1 = "cabbba", word2 = "abbccc"
Output: true

Constraints

1 <= word1.length, word2.length <= 10^5

word1 and word2 contain only lowercase English letters
