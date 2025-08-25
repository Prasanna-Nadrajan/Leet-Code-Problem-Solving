import java.util.*;
class Solution {
    public int[] findDiagonalOrder(int[][] mat) {
        int m=mat.length;
        if(m==0){
            return new int[0];
        }
        int n=mat[0].length;
        int[] res=new int[m*n];
        int k=0;
        for(int i=0;i<m+n-1;i++){
            int t=(i<n)?0:i-n+1,j=(i<n)?i:(n-1);
            if(i%2!=0){
                while(t<m && j>=0){
                    res[k++]=mat[t][j];
                    t++;
                    j--;
                }
            }
            else{
                List<Integer> arr=new ArrayList<>();
                while(t<m && j>=0){
                    arr.add(mat[t][j]);
                    t++;
                    j--;
                }
                for(int a=0;a<arr.size();a++){
                    res[k++]=arr.get(arr.size()-1-a);
                }
            }
            
        }
        return res;
    }
}
