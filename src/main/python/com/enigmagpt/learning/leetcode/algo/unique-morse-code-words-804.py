class Solution:

    mc_map = {
        'a': ".-",
        'b': "-...",
        'c': "-.-.",
        'd': "-..",
        'e': ".",
        'f': "..-.",
        'g': "--.",
        'h': "....",
        'i': "..",
        'j': ".---",#10
        'k': "-.-",
        'l': ".-..",
        'm': "--",
        'n': "-.",
        'o': "---",
        'p': ".--.",
        'q': "--.-",
        'r': ".-.",
        's': "...",
        't': "-", #20
        'u': "..-",
        'v': "...-",
        'w': ".--",
        'x': "-..-",
        'y': "-.--",
        'z': "--.." #26
    }

    def uniqueMorseRepresentations(self, words: list[str]) -> int:

        out = set()

        for word in words:
            morse_str = ""
            for ch in word:
                morse_str += self.mc_map.get(ch)
            out.add(morse_str)

        return len(out)




Solution.uniqueMorseRepresentations(Solution, ["abcd", "abcd", "dupa", "meeeeeemeeeeeee"])