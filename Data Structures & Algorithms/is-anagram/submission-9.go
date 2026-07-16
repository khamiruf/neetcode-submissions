func isAnagram(s string, t string) bool {
    if len(s) != len(t) {
        return false
    }

    m := make(map[rune]int, len(s))
    
    for _, char := range s {
        m[char]++
    }

    for _, t_char := range t {
        m[t_char]--
        if m[t_char] < 0 {
            return false
        }
    }

    return true
}
