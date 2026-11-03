// RUNTIME 0ms Beats 100.00%
// MEMORY4.95MB Beats40.74%

func abs(x int) int {
    if x < 0 {
        return -x
    }
    return x
}

func minMoves(nums []int) int {
    mx := 0
    res := 0

    for i, v := range nums {
        flag := false
        if v > mx {
            flag = true
        }
        if flag {
            res += abs(mx - v) * i
            mx = v
        } else {
            res += abs(mx - v)
        }
    }

    return res
}
