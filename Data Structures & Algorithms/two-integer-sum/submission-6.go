func twoSum(nums []int, target int) []int {
    m := make(map[int]int, len(nums))
    
    for i, n := range nums {
        comp := target - n
        if _, ok := m[comp]; ok {
            return []int{m[comp], i}
        } else {
            m[n] = i
        }
    }
    return []int{-1,-1}
}
