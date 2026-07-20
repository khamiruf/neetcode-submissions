func groupAnagrams(strs []string) [][]string {
    if len(strs) == 0 {
        return [][]string{}
    }

    // Pre-allocate map capacity to reduce memory reallocation overhead
    anagMap := make(map[[26]int][]string, len(strs))

    for _, s := range strs {
        bucket := [26]int{}
        
        // Loop by index to read raw bytes instead of decoding UTF-8 runes
        for i := 0; i < len(s); i++ {
            bucket[s[i]-'a']++
        }

        anagMap[bucket] = append(anagMap[bucket], s)
    }
    
    // Pre-allocate the exact size needed for the result slice
    res := make([][]string, 0, len(anagMap))
    for _, v := range anagMap {
        res = append(res, v)
    }
    
    return res
}