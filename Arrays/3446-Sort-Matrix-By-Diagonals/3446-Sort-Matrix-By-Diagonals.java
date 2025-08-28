import java.util.*;
class Solution {
    public int[][] sortMatrix(int[][] grid) {
        int n=grid.length;
        if(n==0){
            return new int[0][0];
        }
        else if(n==1){
            return grid;
        }
        int c=1;
        int i=n-1;
        while(i>=0){
            int t=i;
            int j=0;
            Integer[] tar=new Integer[c];
            while(t<n && j<n){
                tar[j]=grid[t][j];
                t++;
                j++;
            }
            Arrays.sort(tar,Collections.reverseOrder());
            t=i;
            j=0;
            while(t<n && j<n){
                grid[t][j]=tar[j];
                t++;
                j++;
            }
            i--;
            c++;
        }
        int j=1;
        c=n-1;
        while(j<n){
            int t=j;
            i=0;
            Integer[] tar=new Integer[c];
            while(t<n && i<n){
                tar[i]=grid[i][t];
                t++;
                i++;
            }
            Arrays.sort(tar);
            t=j;
            i=0;
            while(t<n && i<n){
                grid[i][t]=tar[i];
                t++;
                i++;
            }
            j++;
            c--;
        }
        return grid;
    }
}
