import java.util.*;
class Solution {
    public int minEatingSpeed(int[] piles, int h) {
        int j=piles[0];
        for(int pile :piles) if(pile>j) j=pile;
        int i=1;
        while(i<j){
            int mid=(i+j)/2;
            int hours=0;
            for(int pile:piles){
                hours+=(pile+mid-1)/mid;
            }
            if(hours <=h) j=mid;
            else i=mid+1;
        }
        return i;
    }
}
