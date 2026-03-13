class Solution {
    public int[] decrypt(int[] code, int k) {
        if(k==0){
            return new int[code.length];
        }
        int[] res=new int[code.length];
        int n=code.length;
        for(int i=0;i<n;i++){
            int t=0;
            if (k<0){
                for(int j=i-1;j>i+k-1;j--){
                    if(j>=0){
                        t+=code[j%n];
                    }
                    else{
                        t+=code[n+j];
                    }
                }
            }
            else{
                for(int j=i+1;j<i+1+k;j++){
                    t+=code[j%n];
                }
            }
            res[i]=t;
        }
        return res;
    }
}
