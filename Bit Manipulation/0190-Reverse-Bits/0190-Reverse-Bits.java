class Solution {
    public int reverseBits(int n) {
        int j=31,res2=0;
        for(int i=0;i<32;i++){
            res2 <<= 1;
            res2 |= (n&1);
            n >>>= 1;
        }
        return(res2);
    }
}
