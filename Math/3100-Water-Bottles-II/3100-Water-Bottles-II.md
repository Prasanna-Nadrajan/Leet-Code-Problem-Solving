# 3100. Water Bottles II

## Problem Description

You are given two integers `numBottles` and `numExchange`.

`numBottles` represents the number of full water bottles that you initially have. In one operation, you can perform one of the following operations:

1.  Drink any number of full water bottles turning them into empty bottles.
2.  Exchange `numExchange` empty bottles with one full water bottle. Then, increase `numExchange` by one.

**Note** that you cannot exchange multiple batches of empty bottles for the same value of `numExchange`. For example, if `numBottles == 3` and `numExchange == 1`, you cannot exchange 3 empty water bottles for 3 full bottles.

Return the **maximum** number of water bottles you can drink.

### Examples

#### Example 1:
**Input:** `numBottles = 13, numExchange = 6`
**Output:** `15`
**Explanation:** The process is shown below:

| Full Bottles | Empty Bottles | numExchange | Drunk Bottles | Operation |
| :----------: | :-----------: | :---------: | :-----------: | :-------: |
| 13 | 0 | 6 | 0 | **Initial** |
| 0 | 13 | 6 | 13 | **Drink 13** |
| 1 | 7 | 7 | 14 | **Exchange 6** |
| 0 | 8 | 7 | 14 | **Drink 1** |
| 1 | 1 | 8 | 15 | **Exchange 7** |
| 0 | 2 | 8 | 15 | **Drink 1** |
| - | - | 8 | 15 | **End** (Empty < 8) |

#### Example 2:
**Input:** `numBottles = 10, numExchange = 3`
**Output:** `13`
**Explanation:** The process is shown below:

| Full Bottles | Empty Bottles | numExchange | Drunk Bottles | Operation |
| :----------: | :-----------: | :---------: | :-----------: | :-------: |
| 10 | 0 | 3 | 0 | **Initial** |
| 0 | 10 | 3 | 10 | **Drink 10** |
| 1 | 7 | 4 | 11 | **Exchange 3** |
| 0 | 8 | 4 | 11 | **Drink 1** |
| 1 | 4 | 5 | 12 | **Exchange 4** |
| 0 | 5 | 5 | 12 | **Drink 1** |
| 1 | 0 | 6 | 13 | **Exchange 5** |
| 0 | 1 | 6 | 13 | **Drink 1** |
| - | - | 6 | 13 | **End** (Empty < 6) |

### Constraints:
- `1 <= numBottles <= 100`
- `1 <= numExchange <= 100`
