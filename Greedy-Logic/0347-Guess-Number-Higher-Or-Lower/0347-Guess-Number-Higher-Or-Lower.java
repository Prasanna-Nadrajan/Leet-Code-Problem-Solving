/** 
 * Forward declaration of guess API.
 * @param  num   your guess
 * @return 	     -1 if num is higher than the picked number
 *			      1 if num is lower than the picked number
 *               otherwise return 0
 * int guess(int num);
 */

public class Solution extends GuessGame {
    int rec(int st,int end){
        if(st<=end){
            int i=st+(end-st)/2;
            int g=guess(i);
            if(g==0){
                return i;
            }
            else if(g==1){
                return rec(i+1,end);
            }
            else{
                return rec(st,i-1);
            }
        }
        return -1;
    }
    public int guessNumber(int n) {
        return rec(1,n);
    }
}
