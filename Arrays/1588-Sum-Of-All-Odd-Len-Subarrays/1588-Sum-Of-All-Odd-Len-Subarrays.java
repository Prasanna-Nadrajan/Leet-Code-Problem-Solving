import java.util.Arrays;
class Solution {
    public int sumOddLengthSubarrays(int[] arr) {
        int sum=0;
        int[] ps=new int[arr.length+1];
        ps[0]=0;
        for(int i=1;i<=arr.length;i++){
            ps[i]=arr[i-1]+ps[i-1];
        }
        for(int i=0;i<=arr.length;i++){
            for(int j=i+1;j<=arr.length;j+=2){
                sum+=ps[j]-ps[i];
            }
        }
        return sum;
    }
}
