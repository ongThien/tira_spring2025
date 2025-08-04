class WordFinder:
    def set_grid(self, grid):
        self.grid = grid
        self.rows = len(grid)
        self.cols = len(grid[0]) if self.rows > 0 else 0

    def count(self, word):
        word_len = len(word)

        # For single letter word, count all letter occurrences in entire grid
        if word_len == 1:
            return sum(row.count(word) for row in self.grid)

        # Only 4 directions: right, down, down-right, down-left
        # These cover all directions uniquely
        directions = [
            (0, 1),  # right
            (1, 0),  # down
            (1, 1),  # down-right diagonal
            (1, -1),  # down-left diagonal
        ]

        def in_bounds(r, c):
            return 0 <= r < self.rows and 0 <= c < self.cols

        count = 0
        for r in range(self.rows):
            for c in range(self.cols):
                for dr, dc in directions:
                    end_r = r + dr * (word_len - 1)
                    end_c = c + dc * (word_len - 1)
                    if not in_bounds(end_r, end_c):
                        continue

                    # Extract the sequence
                    seq_chars = []
                    for i in range(word_len):
                        rr = r + dr * i
                        cc = c + dc * i
                        seq_chars.append(self.grid[rr][cc])
                    seq = "".join(seq_chars)

                    # Check if the word matches forwards or backwards
                    if seq == word or seq[::-1] == word:
                        count += 1

        return count


if __name__ == "__main__":
    grid = ["TIRATIRA", "IRATIRAT", "RATIRATI", "ATIRATIR"]

    finder = WordFinder()
    finder.set_grid(grid)

    print(finder.count("TIRA"))  # 7
    print(finder.count("TA"))  # 13
    print(finder.count("RITARI"))  # 3
    print(finder.count("A"))  # 8
    print(finder.count("AA"))  # 6
    print(finder.count("RAITA"))  # 0
