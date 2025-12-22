class Solution {
    public int[] productExceptSelf(int[] nums) {
        int n=nums.length;
        int[] sa=new int[n];
        int[] pa=new int[n];
        sa[n-1]=1;
        for(int i=n-2;i>=0;i--){
            sa[i]=sa[i+1]*nums[i+1];
        }
        
        pa[0]=1;
        for(int i=1;i<n;i++){
            pa[i]=pa[i-1]*nums[i-1];
        }
        for(int i=0;i<n;i++){
            nums[i]=sa[i]*pa[i];
        }
        return nums;
    }
}
