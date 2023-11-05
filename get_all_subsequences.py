class Solution:
    def get_all_subsequences(self, string):
        self.string = string
        self.n = len(string)

        self.subsequences = set()
        self._get_all_subsequences(0, "")
        return self.subsequences

    def _get_all_subsequences(self, i, output):
        if (i == self.n):
            self.subsequences.add(output)
            return None
        self._get_all_subsequences(i+1, output+self.string[i])
        self._get_all_subsequences(i+1, output)
        return None

if __name__ == "__main__":
    string = "abc"
    solution = Solution()
    subsequences = solution.get_all_subsequences(string)
    print(subsequences)