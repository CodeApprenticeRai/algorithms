# Adapted from https://www.geeksforgeeks.org/find-possible-words-phone-digits/

class Solution:
    def words_from_digits(self, user_input: str) -> list[str]:
        self.hash_table = [
            "","","abc","def","ghi","jkl",
            "mno", "pqrs", "tuv", "wxyz"
        ]
        self.words = []

        self.fmtd_user_input = [int(user_input[i]) for i in range(len(user_input))]
        self.n = len(fmtd_user_input)

        return self._words_from_digits(0, [])
    
    def _words_from_digits(self, i, output):
        if (i == self.n):
            self.words.append(output)
            return None

        keypad_letters_for_i = self.hashTable[self.fmtd_user_input[i]]
        for j in range(len(keypad_letters_for_i)):
            output.append(keypad_letters_for_i[j])
            self._words_from_digits(i+1, output)
            output.pop()
            if self.fmtd_user_input[i] in [0,1]:
                return None
        
if __name__ == "__main__":
    solution = Solution()

    user_input = "234"
    words = solution.words_from_digits(user_input)
    print(words)