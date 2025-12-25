import java.util.*;

class Solution {
    public int maxOperations(int[] nums, int k) {
        Arrays.sort(nums);
        int l=0,r=nums.length-1,c=0;
        while(l<r){
            int s=nums[l]+nums[r];
            if(s==k){
                c++;
                l++;
                r--;
            }
            else if(s>k){
                r--;
            }
            else if(s<k){
                l++;
            }
        }
        return c;
    }
}
