import java.util.*;
class Solution {
    public int[] asteroidCollision(int[] asteroids) {
        Stack<Integer> ss=new Stack<>();
        for(int i:asteroids){
            boolean a=true;
            while(a && !ss.empty() && ss.peek()>0 && i<0){
                int last=ss.peek();
                if(Math.abs(last)<Math.abs(i)){
                    ss.pop();
                }
                else if(Math.abs(last)==Math.abs(i)){
                    ss.pop();
                    a=false;
                }
                else{
                    a=false;
                }
            }
            if(a){
                ss.push(i);
            }
        }
        int[] ans=new int[ss.size()];
        for(int i=0;i<ans.length;i++) ans[i]=ss.get(i);
        return ans;
    }
}
