// RUNTIME: 100.00%
// MEMORY:  92.00%
func minAddToMakeValid(s string) int {
    stck := []byte{}

    for _, r := range s {
        if r == '(' {
            stck = append(stck, byte(r))
        } else {
            if len(stck) == 0 || stck[len(stck) - 1] == byte(r) {
                stck = append(stck, byte(r))
            } else {
                stck = stck[:len(stck) - 1]
            }
        }
    }

    return len(stck)
}
