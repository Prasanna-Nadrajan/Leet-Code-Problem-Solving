class Solution {
    public long flowerGame(int n, int m) {
        long odd_x=(n+1)/2;
        long even_x=n/2;
        long odd_y=(m+1)/2;
        long even_y=m/2;
        return odd_x*even_y+odd_y*even_x;
    }
}
