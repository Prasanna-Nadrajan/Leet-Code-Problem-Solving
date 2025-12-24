import java.util.*;
class Solution {
    public int minimumBoxes(int[] apple, int[] capacity) {
        Arrays.sort(capacity);
        int c=1,cap=capacity.length-1;
        int sc=0;
        int sapp=0;
        for(int i=0;i<apple.length;i++) sapp+=apple[i];
        while(cap>=0 && sc+capacity[cap]<sapp){
            sc+=capacity[cap];
            cap--;
            c+=1;
        }
        return c;

    }
}
