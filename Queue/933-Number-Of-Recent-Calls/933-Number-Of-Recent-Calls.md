# 933. Number of Recent Calls

You have a `RecentCounter` class which counts the number of recent requests within a certain time frame.

Implement the `RecentCounter` class:

- `RecentCounter()` initializes the counter with zero recent requests.
- `int ping(int t)` adds a new request at time `t`, where `t` represents some time in milliseconds, and returns the number of requests that have happened in the past `3000` milliseconds (including the new request).

Specifically, return the number of requests that have happened in the inclusive range `[t - 3000, t]`.

It is guaranteed that every call to `ping` uses a **strictly larger value of `t`** than the previous call.

---

## Example 1

Input:
["RecentCounter", "ping", "ping", "ping", "ping"]
[[], [1], [100], [3001], [3002]]

makefile
Copy code

Output:
[null, 1, 2, 3, 3]

yaml
Copy code

---

## Explanation

- `RecentCounter()` initializes the counter.
- `ping(1)` → 1 request in range `[-2999, 1]`
- `ping(100)` → 2 requests in range `[-2900, 100]`
- `ping(3001)` → 3 requests in range `[1, 3001]`
- `ping(3002)` → 3 requests in range `[2, 3002]`

---

## Constraints

- `1 <= t <= 10^9`
- Each test case will have at most `10^4` calls to `ping`
