class Solution {
    public int largestAltitude(int[] gain) {
        int max=0;
        int f=0;
        for(int i=0;i<gain.length;i++){
            f=f+gain[i];
            max=(max<f)?f:max;
        }
        return max;
    }
}
