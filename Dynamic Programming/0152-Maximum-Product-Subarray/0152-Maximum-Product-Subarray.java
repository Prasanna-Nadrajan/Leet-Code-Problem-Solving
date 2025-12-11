import java.util.*;
class Solution {
    public int maxProduct(int[] arr) {
        // answer
        int n=arr.length;
        int[] maxi=new int[n];
        int[] mini=new int[n];
        maxi[0]=arr[0];
        mini[0]=arr[0];
        int m=arr[0];
        for(int i=1;i<n;i++){
            maxi[i]=Math.max(Math.max(arr[i],maxi[i-1]*arr[i]),mini[i-1]*arr[i]);
            mini[i]=Math.min(Math.min(arr[i],maxi[i-1]*arr[i]),mini[i-1]*arr[i]);
            if(m<maxi[i]){
                m=maxi[i];
            }
        }
        return m;
    }
}
