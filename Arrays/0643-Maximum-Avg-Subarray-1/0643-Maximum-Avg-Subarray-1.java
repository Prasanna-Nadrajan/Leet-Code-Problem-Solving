class Solution {
    static double sum(int[] nums,int i,int j){
        double s=0;
        for(int k=i;k<=j;k++){
            s+=nums[k];
        }
        return s;
    }
    public double findMaxAverage(int[] nums, int k) {
        int n=nums.length,i=0,j=k-1;
        double s=sum(nums,i,j);
        double a=s/k;
        i++;j++;
        while(j<n){
            s=(s-nums[i-1]+nums[j]);
            double at= s/k;
            a=(at>a)?at:a;
            i++;
            j++;
        }
        return a;
    }
}
