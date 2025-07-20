class Solution {
    public int consecutiveNumbersSum(int n) {
        int count=0;
        for(int i=1;i<Math.sqrt(2*n);i++){
            if((2*n)%i==0){
                int m=(2*n)/i;
                if((m-i+1)%2==0){
                    int k=(m-i+1)/2;
                    if(k>0){
                        count++;
                    }
                }
            }

        }
        return count;
    }
}