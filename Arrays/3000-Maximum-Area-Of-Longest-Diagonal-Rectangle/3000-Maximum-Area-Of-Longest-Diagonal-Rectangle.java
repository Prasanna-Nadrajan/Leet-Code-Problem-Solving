class Solution {
    public int areaOfMaxDiagonal(int[][] dimensions) {
        double max=0;
        int area=0;
        for(int i=0;i<dimensions.length;i++){
            int len=dimensions[i][0];
            int wid=dimensions[i][1];
            double diag=Math.sqrt((len*len)+(wid*wid));
            if(max<=diag){
                if(max==diag){
                    area=((len*wid)>area)?(len*wid):area;
                }
                else{
                    area=len*wid;
                }
                max=diag;
            }
        }
        return area;
    }
}
