class Solution {
    public int countHillValley(int[] nums) {
        int count=0;
        int len=nums.length;
        System.out.println(len);
        int ls;
        int rs;
        for(int i=1;i<len;i++){
            int tok=nums[i];
            if(nums[i]==nums[i-1]){
                continue;
            }
            int j=i-1;
            while(j>=0 && nums[j]==nums[i]){
                j--;
            }
            if(j<0){
                continue;
            }
            ls=nums[j];
            j=i+1;
            while(j<len && nums[i]==nums[j]){
                j++;
            }
            if(j==len){
                continue;
            }
            rs=nums[j];
            if((tok>ls && tok>rs) ||(tok<ls && tok<rs)){
                count++;
            }
        }
        return count;
    }
}
