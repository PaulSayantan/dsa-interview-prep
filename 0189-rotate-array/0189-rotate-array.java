class Solution {
    public void rotate(int[] nums, int k) {
        int n = nums.length;
        k = k % n;
        // we have to first reverse first half of the array
        reverse(nums, 0, n-k-1);
        // then reverse the second half of the array
        reverse(nums, n-k, n-1);
        // at the end reverse the entire array
        reverse(nums, 0, n-1);
    }
    public void reverse(int[] nums, int start, int end) {
        while (start < end) {
            int temp = nums[start];
            nums[start] = nums[end];
            nums[end] = temp;
            start++;
            end--;
        }
    }
}