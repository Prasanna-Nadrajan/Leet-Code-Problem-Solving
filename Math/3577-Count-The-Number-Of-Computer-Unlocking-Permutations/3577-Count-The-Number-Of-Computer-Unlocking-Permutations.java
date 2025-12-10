import java.util.*;

class Solution {
    public int countPermutations(int[] complexity) {
        int f=complexity[0];
        int min=f;
        int freq=0;
        for(int i:complexity){
            if(i<min){
                min=i;
            }
            if(i==f){
                freq+=1;
            }
        }
        if(min!=f || freq!=1){
            return 0;
        }
        long mod=1000000007;
        long ans=1;
        long n=complexity.length-1;
        while(n>1){
            ans*=n;
            ans%=mod;
            n--;
        }
        ans%=mod;
        return (int)ans;

    }
}
