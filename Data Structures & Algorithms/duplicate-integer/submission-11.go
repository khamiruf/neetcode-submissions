func hasDuplicate(nums []int) bool {
    numSet := make(map[int]struct{})

    for _, n := range nums {
        if _, exists := numSet[n]; exists {
            return true
        } else {
            numSet[n] = struct{}{}
        }
    }

    return false
}
