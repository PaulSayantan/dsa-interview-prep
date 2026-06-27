func findMin(nums []int) int {
    low := 0
    high := len(nums) - 1

    if nums[low] <= nums[high] {
        return nums[low]
    }

    mini := 9999

    for low <= high {
        mid := low + (high - low) / 2
        if nums[low] <= nums[mid] {
            mini = min(mini, nums[low])
            low = mid + 1
        } else {
            mini = min(mini, nums[mid])
            high = mid - 1
        }
    }

    return mini
}