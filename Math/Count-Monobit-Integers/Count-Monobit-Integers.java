class Solution {
    static boolean check(int num){
        while(num!=0){
            if(num==1) return true;
            if(num%2!=0) return false;
            num/=2;
        }
        return true;
    }
    public int countMonobit(int n) {
        if(n<=1) return n+1;
        int ans=2;
        for(int i=2;i<=n;i++){
            if(check(i+1)) ans++;
        }
        return ans;
    }
    
}
