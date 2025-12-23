class Solution {
    public void moveZeroes(int[] nums) {
        int n=nums.length;
        int lnz=0;
        for(int i=0;i<n;i++){
            if(nums[i]!=0){
                nums[lnz]=nums[i];
                lnz++;
            }
        }
        for(int i=lnz;i<n;i++){
            nums[i]=0;
        }
    }
}
