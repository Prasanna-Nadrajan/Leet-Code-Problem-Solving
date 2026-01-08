class Solution {
    public int tribonacci(int n) {
        if(n==0) return 0;
        else if(n==1||n==2) return 1;
        List<Integer> arr=new ArrayList<>();
        arr.add(0);
        arr.add(1);
        arr.add(1);
        for(int i=3;i<n+1;i++){
            arr.add(arr.get(i-1)+arr.get(i-2)+arr.get(i-3));
        }
        return arr.get(n);
    }
}
