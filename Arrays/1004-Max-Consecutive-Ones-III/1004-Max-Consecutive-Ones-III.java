class Solution {
    public int longestOnes(int[] nums, int k) {
        int l=0;
        int r=0;
        int maxlen=0;
        int zero=0;
        for(r=0;r<nums.length;r++){
            if(nums[r]==0){
                zero++;
            }
            while(zero>k){
                if(nums[l]==0){
                    zero--;
                }
                l++;
            }
            maxlen=(maxlen>(r-l+1))?maxlen:(r-l+1);
        }

        return maxlen;
    }
}
