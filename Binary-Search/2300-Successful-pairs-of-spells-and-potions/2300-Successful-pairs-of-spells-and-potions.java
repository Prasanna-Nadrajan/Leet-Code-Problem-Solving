import java.util.Arrays;
class Solution {
    public int[] successfulPairs(int[] spells, int[] potions, long success) {
        Arrays.sort(potions);
        int l=potions.length;
        int s=spells.length;
        int[] ans=new int[s];
        for(int i=0;i<s;i++){
            int idx=l;
            int left=0;
            int right=l-1;
            int spell=spells[i];
            while(left<=right){
                int mid=left+(right-left)/2;
                if((long)spell*potions[mid]>=success){
                    idx=mid;
                    right=mid-1;
                }
                else{
                    left=mid+1;
                } 
            }
            ans[i]=l-idx;
        }
        return ans;
    }
}
