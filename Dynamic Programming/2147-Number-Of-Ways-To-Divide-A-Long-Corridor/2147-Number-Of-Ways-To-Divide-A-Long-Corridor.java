import java.util.*;
class Solution {
    public int numberOfWays(String corridor) {
        long mod=1000000000+7;
        List<Integer> arr=new ArrayList<>();
        for(int i=0;i<corridor.length();i++){
            if(corridor.charAt(i)=='S'){
                arr.add(i);
            }
        }
        int s=arr.size();
        if(s==0 || s%2!=0){
            return 0;
        }
        long ans=1;
        for(int i=2;i<s;i+=2){
            long gap=arr.get(i)-arr.get(i-1);
            ans=((gap*ans)%mod);
        }
        return (int)ans;
    }
}
