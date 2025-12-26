class Solution {
    static int partition(int l,int r, int[] nums){
        int pivot=l;
        int left=l+1;
        int right=r;
        int t;
        while(left<=right){
            while(left<=right && nums[pivot]<nums[left]){
                left++;
            }
            while(left<=right && nums[pivot]>nums[right]){
                right--;
            }
            if(left<=right){
                t=nums[left];
                nums[left]=nums[right];
                nums[right]=t;
                left++;
                right--;
            }
        }
        t=nums[pivot];
        nums[pivot]=nums[right];
        nums[right]=t;
        return right; 
    }
    
    static int quickSelect(int l,int r,int[] nums,int k){
        if(l<=r){
            int ind=partition(l,r,nums);
            if(ind==k){
                return nums[ind];
            }
            else if(ind>k){
                return quickSelect(l,ind-1,nums,k);
            }
            else if(ind<k){
                return quickSelect(ind+1,r,nums,k);
            }
        }
        return -1;
    } 
    
    public int findKthLargest(int[] nums, int k) {
        int left=0;
        int right=nums.length-1;
        int kth=quickSelect(left,right,nums,k-1);
        return kth;
    }
}
