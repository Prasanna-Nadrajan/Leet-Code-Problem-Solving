443. String Compression

Difficulty: Medium
Topics: Two Pointers, String

Problem Statement

Given an array of characters chars, compress it using the following algorithm:

Start with an empty string s.

For each group of consecutive repeating characters:

If the group length is 1, append the character to s.

Otherwise, append the character followed by the group's length.

The compressed string is stored directly in the input array chars.

Return the new length of the modified array.

Characters beyond the returned length do not matter and should be ignored.

Examples

Input: ["a","a","b","b","c","c","c"]
Output: 6 → ["a","2","b","2","c","3"]

Input: ["a"]
Output: 1 → ["a"]

Input: ["a","b","b","b","b","b","b","b","b","b","b","b","b"]
Output: 4 → ["a","b","1","2"]

Constraints

1 <= chars.length <= 2000

chars[i] may be letters, digits, or symbols

Requirement

The solution must use constant extra space.
