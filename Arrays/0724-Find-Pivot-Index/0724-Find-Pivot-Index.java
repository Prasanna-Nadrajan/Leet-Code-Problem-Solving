import java.util.*;
class Solution {
    public int pivotIndex(int[] nums) {
        int[] rl=new int[nums.length];
        int[] ll=new int[nums.length];
        ll[0]=nums[0];
        rl[nums.length-1]=nums[nums.length-1];
        for(int i=1;i<nums.length;i++){
            ll[i]=nums[i]+ll[i-1];
            rl[nums.length-1-i]=nums[nums.length-i-1]+rl[nums.length-i];
        }
        for (int i=0;i<nums.length;i++){
            if(ll[i]==rl[i]){
                return i;
            }
        }
        return -1;

    }
}
