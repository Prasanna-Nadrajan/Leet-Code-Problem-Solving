import java.util.*;
class Solution {
    public int threeSumClosest(int[] nums, int target) {
        int n=nums.length;
        Arrays.sort(nums);
        int tot=nums[0]+nums[1]+nums[n-1];
        for(int i=0;i<n;i++){
            int j=i+1;
            int k=n-1;
            while(j<k){
                int t=(nums[i]+nums[j]+nums[k]);
                if(t>target){
                    k--;
                }
                else{
                    j++;
                }
                tot=(Math.abs(tot-target)>Math.abs(t-target))?t:tot;
            }
        }
        return tot;
    }
}
