func longestConsecutive(nums []int) int {
    numSet := make(map[int]struct{}, len(nums))
    for _, n := range nums {
        numSet[n] = struct{}{}
    }

    longest := 0
    for _, num := range nums {
        if _, ok := numSet[num-1]; !ok {
            // this is the start of the seq
            x := num
            length := 1
            for {
                if _, ok := numSet[x+1]; !ok {
                    break
                }
                x++
                length++
            }
            if (length > longest) {
                longest = length
            }
        }
    }
    return longest
}
