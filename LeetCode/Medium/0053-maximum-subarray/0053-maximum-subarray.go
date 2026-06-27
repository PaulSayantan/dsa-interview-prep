func maxSubArray(nums []int) int {
    maxi := -10001
    add := 0
    for i := 0; i < len(nums); i++ {
        add = add + nums[i]
        if add > maxi {
            maxi = add
        }
        if add < 0 {
            add = 0
        }
    }

    return maxi
}