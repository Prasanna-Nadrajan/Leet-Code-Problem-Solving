class Solution {
    public int countTriples(int n) {
        int count=0;
        for(int i=3;i<=n;i++){
            for(int j=i+1;j<=n;j++){
                int c=i*i+j*j;
                double s=Math.sqrt(c);
                if(s<=n && (int)s*(int)s==c){
                    count+=2;
                }
            }
        }
        return count;
    }
}
