// RUNTIME : 25ms/61.54%
// MEMORY  : 19.02MB/7.69%

func maxAlternatingSum(nums []int) int64 {
    for i := 0; i < len(nums); i++ {
        nums[i] *= nums[i]
    }

    sort.Ints(nums)

    res := 0
    for i := 0; i < len(nums); i++ {
        if i < len(nums) / 2 {
            res -= nums[i]
        } else {
            res += nums[i]
        }
    }

    return int64(res)
}
