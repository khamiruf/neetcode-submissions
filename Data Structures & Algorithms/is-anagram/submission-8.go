func isAnagram(s string, t string) bool {
    if len(s) != len(t) {
        return false
    }

    m := make(map[rune]int, len(s))
    
    for _, char := range s {
        m[char]++
    }

    for _, t_char := range t {
        if _, ok := m[t_char]; ok {
            m[t_char]--
        } else {
            return false
        }
    }

    for _, v := range m {
        if v != 0 {
            return false
        }
    }

    return true
}
