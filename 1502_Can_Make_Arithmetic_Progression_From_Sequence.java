import java.util.Arrays;
class Solution {
    public boolean canMakeArithmeticProgression(int[] arr) {
        Arrays.sort(arr);
        int slope = arr[1] - arr[0];
        int holdme = 0;
        for(int i=2; i<arr.length; i++){
            holdme=arr[i] - arr[i-1];
            if(holdme!=slope){ 
                return false;
            }
        }
        return true;
    }   
}