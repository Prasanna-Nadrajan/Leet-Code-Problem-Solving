class Solution:
    def sumAndMultiply(self, s: str, queries: List[List[int]]) -> List[int]:
        mod = 10**9 + 7
        n = len(s)

        prefix_sum = [0] * (n+1)    
        prefix_val = [0] * (n+1)   
        prefix_count = [0] * (n+1)  

        for i in range(n):
            d = int(s[i])
            prefix_sum[i+1] = prefix_sum[i]
            prefix_val[i+1] = prefix_val[i]
            prefix_count[i+1] = prefix_count[i]
            if d != 0:
                prefix_sum[i+1] += d
                prefix_val[i+1] = (prefix_val[i] * 10 + d) % mod
                prefix_count[i+1] += 1

        pow10 = [1] * (n+1)
        for i in range(1, n+1):
            pow10[i] = (pow10[i-1] * 10) % mod

        def calc(l, r):
            dsum = prefix_sum[r+1] - prefix_sum[l]
            cnt = prefix_count[r+1] - prefix_count[l]
            val = (prefix_val[r+1] - prefix_val[l] * pow10[cnt]) % mod
            return (val * dsum) % mod

        return [calc(l, r) for l, r in queries]
