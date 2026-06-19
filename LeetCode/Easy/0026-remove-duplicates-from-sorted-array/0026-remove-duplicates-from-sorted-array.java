class Solution {
    public int removeDuplicates(int[] nums) {
        // item at 0th index will never get replaced, it's already at sorted position
        if (nums.length == 1) {
            return 1;
        }
        if (nums.length == 2) {
            if (nums[0] == nums[1]) {
                return 1;
            }
            return 2;
        }
        // start iteration from 1st index.
        int i = 0;
        for (int j = 1; j < nums.length; j++) {
            if (nums[i] < nums[j]) {
                nums[i+1] = nums[j];
                i++;
            }
        }

        return i+1;
    }
}