class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        morse = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..",
                 "--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-",
                 "-.--","--.."]
        alaphabet = string.ascii_lowercase
        mapping = {c: v for c, v in zip(alaphabet, morse)}
        morse_words = set()
        for word in words:
            morse_word = ""
            for c in word:
                morse_word += mapping[c]
            morse_words.add(morse_word)
        return len(morse_words)