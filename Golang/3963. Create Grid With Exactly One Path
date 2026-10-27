// RUNTIME 0ms Beats 100.00%
// MEMORY 5.89MB Beats 100.00%
func createGrid(m int, n int) []string {
    r := make([]string, 0, m)
    var sb1 strings.Builder
    var sb2 strings.Builder

    sb1.Grow(n)
    sb2.Grow(n)

    for i := 0; i < n ; i++ {
        sb1.WriteRune('.')
        if i + 1 != n {
            sb2.WriteRune('#')
        } else {
            sb2.WriteRune('.')
        }
    }
    
    r = append(r, sb1.String())
    for i := 0; i < m - 1 ; i++ {
        r = append(r, sb2.String())
    }

    return r
}
