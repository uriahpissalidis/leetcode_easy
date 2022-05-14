import java.util.Arrays;
class Solution {
    public List<Boolean> kidsWithCandies(int[] candies, int extraCandies) {
        List<Boolean> ans = new ArrayList<>(candies.length);
        int max = 0;
        for (int candy : candies) {
            max = Math.max(candy, max);
        }
        for (int candy : candies) {
            ans.add(candy + extraCandies >= max);
        }
        return ans;
        /*
        int maxCandy = 0; //store max element in here
        for(int i=0; i<candies.length; i++){
            if(maxCandy <= candies[i]) maxCandy = candies[i];
        }

        Boolean[] tfArray = new Boolean[candies.length];
        
        for(int i=0; i<candies.length; i++){
            System.out.println(candies[i] + " <= " + extraCandies);
            if(maxCandy <= (candies[i]+extraCandies)){
                tfArray[i] = true;
            }
            else{
                tfArray[i] = false;
            }
        }
        List<Boolean> list = Arrays.asList(tfArray);
        return list;
        */
    }
}