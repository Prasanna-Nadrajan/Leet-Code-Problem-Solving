# 3433. Count Mentions Per User

## Problem Statement

You are given an integer `numberOfUsers` representing the total number of users and a list of events, where each event is of the form `[type, timestamp, value]`.

Each event is one of the following:

### 1. MESSAGE Event

`["MESSAGE", timestamp, mentions_string]`

This event indicates that a message was sent at `timestamp` and mentions a set of users. The `mentions_string` can contain:

* `id<number>`: Mentions a specific user. There may be multiple ids, separated by spaces, and duplicates are allowed.
* `ALL`: Mentions **all users**, including offline users.
* `HERE`: Mentions **only users who are currently online**.

Each mention must be counted separately, even if a user is mentioned multiple times in the same message.

### 2. OFFLINE Event

`["OFFLINE", timestamp, id]`

This event indicates that the user `id` goes offline at `timestamp` for exactly 60 time units. The user automatically comes back online at `timestamp + 60`.

## Important Rules

* All users are initially online.
* Any online/offline status changes at a given timestamp are processed **before** handling MESSAGE events at the same timestamp.
* Offline users can still be mentioned via `ALL` or direct `id<number>` mentions.

## Task

Return an array `mentions` where `mentions[i]` represents the total number of times user `i` was mentioned across all MESSAGE events.

---

## Examples

### Example 1

**Input:**

```
numberOfUsers = 2
events = [["MESSAGE","10","id1 id0"], ["OFFLINE","11","0"], ["MESSAGE","71","HERE"]]
```

**Output:**

```
[2, 2]
```

### Example 2

**Input:**

```
numberOfUsers = 2
events = [["MESSAGE","10","id1 id0"], ["OFFLINE","11","0"], ["MESSAGE","12","ALL"]]
```

**Output:**

```
[2, 2]
```

### Example 3

**Input:**

```
numberOfUsers = 2
events = [["OFFLINE","10","0"], ["MESSAGE","12","HERE"]]
```

**Output:**

```
[0, 1]
```

---

## Constraints

* `1 <= numberOfUsers <= 100`
* `1 <= events.length <= 100`
* `1 <= timestamp <= 10^5`
* Each MESSAGE contains between 1 and 100 mentions
* User IDs are in the range `[0, numberOfUsers - 1]`
* The user referenced in an OFFLINE event is guaranteed to be online at that time
