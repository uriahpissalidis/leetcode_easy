class Solution {
    public int removeDuplicates(int[] nums) {
        int left = 1; //this variable also keeps track of the unique number of integers in the array
        for(int i=1; i<nums.length; i++){
            if(nums[i] != nums[i-1]){ //if values are different
                nums[left] = nums[i]; //replace them here
                left++; //replacement variable is iterated upon
            }
        }
        return left;
    }
}