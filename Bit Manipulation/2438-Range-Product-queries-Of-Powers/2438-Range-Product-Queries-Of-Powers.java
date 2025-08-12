import java.util.*;
class Solution {
    public int[] productQueries(int n, int[][] queries) {
        List<Integer> arr=new ArrayList<>();
        int[] res=new int[queries.length];
        for(int i=0;n!=0;i++){
            if((n&1)==1){
                arr.add(1<<i);
            }
            n>>=1;
        }

        for(int j=0;j<queries.length;j++){
            long temp=1;
            for(int i=queries[j][0];i<=queries[j][1];i++){
                temp*=arr.get(i);
                temp%=(int)Math.pow(10,9)+7;
            }
            temp%=(int)(Math.pow(10,9)+7);
            res[j]=(int)temp;
        }
        return res;
    }
}
