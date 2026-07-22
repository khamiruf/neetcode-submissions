class Solution:

    def encode(self, strs: List[str]) -> str:
        # len, "#"
        res = []
        for s in strs:
            str_len = len(s)
            new_str = str(len(s)) + "#" + s
            res.append(new_str)

        return "".join(res)

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0

        while i < len(s):
            j = i
            while s[j] != '#':
                j += 1

            word_len = int(s[i:j])
            word = s[j+1:j+1+word_len]
            res.append(word)
            i = j + 1 + word_len
        
        return res