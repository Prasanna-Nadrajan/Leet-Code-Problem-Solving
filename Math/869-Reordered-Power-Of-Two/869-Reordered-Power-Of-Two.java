import java.util.Arrays;
class Solution {
    static int count(int n){
        int c=0;
        while(n!=0){
            c++;
            n/=10;
        }
        return c;
    }

    public String toFreq(int num){
        int[] arr=new int[10];
        int c=count(num);
        int t=num;
        for(int i=0;i<c ;i++){

            arr[(int)Math.abs(t%10)]+=1;
            t/=10;
        }
        return Arrays.toString(arr);
    }

    public boolean reorderedPowerOf2(int n) {
        int[] arr=new int[10];
        int inc=1,c=count(n),t=n;
        for(int i=0;i<c;i++){
            arr[(int)Math.abs(t%10)]+=1;
            t/=10;
        }    
        System.out.println(Arrays.toString(arr));
        while(c>count(inc)){
            inc*=2;
        }
        while(c==count(inc)){
            if(Arrays.toString(arr).equals(toFreq(inc))){
                return true;
            }
            inc*=2;
        }
        return false;
    }
}
