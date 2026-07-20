func groupAnagrams(strs []string) [][]string {
    anag_map := make(map[[26]int][]string)

    for _, s := range strs {
        bucket := [26]int{}

        for _, ch := range s {
            idx := int(ch) - int('a')
            bucket[idx]++
        }
        anag_map[bucket] = append(anag_map[bucket], s)
    }
    
    res := [][]string{}
    for _, v := range anag_map {
        res = append(res, v)
    }
    return res
}
