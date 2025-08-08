class Solution {
    double[][] memo;
    public double recurse(int a,int b){

        if(a<=0 && b<=0){
            return 0.5;
        }
        else if(a<=0){
            return 1;
        }
        else if(b<=0){
            return 0;
        }
        if (memo[a][b]!=-1){
            return memo[a][b];
        }
        double p=0;
        int ta,tb;
        ta=(a<=4)?0:(a-4);
        tb=(b<=0)?0:b;
        p+=recurse(ta,tb);
        ta=(a<=3)?0:a-3;
        tb=(b<=1)?0:b-1;
        p+=recurse(ta,tb);
        ta=(a<=2)?0:a-2;
        tb=(b<=2)?0:b-2;
        p+=recurse(ta,tb);
        ta=(a<=1)?0:a-1;
        tb=(b<=3)?0:b-3;
        p+=recurse(ta,tb);
        memo[a][b]=p*0.25;
        return memo[a][b];
    }
    public double soupServings(int n) {
        if (n>=4800){
            return 1;
        }
        int m=(n+24)/25;
        memo=new double[m+1][m+1];
        for(int i=0;i<=m;i++){
            for(int j=0;j<=m;j++){
                memo[i][j]=-1;
            }
        }
        return recurse(m,m);
        
    }
}
