// Runtime: 71.14%
// Memory: 35.90%

type ByFirst [][]int

func (a ByFirst) Len() int { return len(a) }
func (a ByFirst) Less(i, j int) bool { return a[i][0] < a[j][0] }
func (a ByFirst) Swap(i, j int)      { a[i], a[j] = a[j], a[i] }

func merge(intervals [][]int) [][]int {
    if len(intervals) == 1 {
        return intervals
    }
    
    s := make([][]int, 0, len(intervals))

    sort.Sort(ByFirst(intervals))

    endOfSegment := intervals[0][1]
    startOfSegment := intervals[0][0]
    for i := 1; i < len(intervals); i++ {
        if endOfSegment >= intervals[i][0] {
            endOfSegment = max(endOfSegment, intervals[i][1])
        } else {
            s = append(s, []int{startOfSegment, endOfSegment})
            endOfSegment = intervals[i][1]
            startOfSegment = intervals[i][0]
        }

        if i == len(intervals) - 1 {
            s = append(s, []int{startOfSegment, endOfSegment})
        }
    }

    return s
}   
