import java.util.*;
class Solution {
    public int countPartitions(int[] nums, int k) {
        int n=nums.length;
        long mod=1000000007;
        long[] dp=new long[n+1];           
        long[] prefix=new long[n+1];           
        dp[0]=1;
        prefix[0]=1;
        Deque<Integer> minDeque=new ArrayDeque<>();
        Deque<Integer> maxDeque=new ArrayDeque<>();
        int left=0;
        for(int i=0;i<n;i++){
            while(!minDeque.isEmpty() && nums[minDeque.peekLast()]>=nums[i]){
                minDeque.pollLast();
            }
            minDeque.offerLast(i);
            while(!maxDeque.isEmpty() && nums[maxDeque.peekLast()]<=nums[i]){
                maxDeque.pollLast();
            }
            maxDeque.offerLast(i);
            while((nums[maxDeque.peekFirst()]-nums[minDeque.peekFirst()])>k){
                if(minDeque.peekFirst()==left) minDeque.pollFirst();
                if(maxDeque.peekFirst()==left) maxDeque.pollFirst();
                left++;
            }
            dp[i+1]=(prefix[i]-(left>0?prefix[left-1]:0)+mod)%mod;
            prefix[i+1]=(prefix[i]+dp[i+1])%mod;

        }
        return (int)dp[n];
    }
}
