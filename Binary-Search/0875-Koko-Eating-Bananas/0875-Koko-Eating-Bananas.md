875. Koko Eating Bananas

Difficulty: Medium

Problem Statement

Koko loves to eat bananas. There are n piles of bananas, where the i-th pile has piles[i] bananas. The guards will return in h hours.

Koko can decide her eating speed k (bananas per hour). Each hour, she chooses one pile and eats up to k bananas from that pile. If the pile has fewer than k bananas, she eats the entire pile and does not eat any more bananas during that hour.

Koko wants to eat as slowly as possible but must finish all the bananas before the guards return.

Return the minimum integer k such that Koko can eat all the bananas within h hours.

Examples

Example 1
Input: piles = [3,6,7,11], h = 8
Output: 4

Example 2
Input: piles = [30,11,23,4,20], h = 5
Output: 30

Example 3
Input: piles = [30,11,23,4,20], h = 6
Output: 23

Constraints

1 <= piles.length <= 10^4

piles.length <= h <= 10^9

1 <= piles[i] <= 10^9
