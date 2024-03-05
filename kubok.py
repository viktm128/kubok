"""Build a Kubok solver for an arbitrary n x n Kubok.

Ideally run algorithm analysis and verify performance with a test bench.
"""


class Kubok:
    """Host Kubok solver infrastructure."""

    def __init__(self, f_name):
        """Initiate board from file."""
        with open(f_name, "r", encoding="utf-8") as f_obj:

            self.n = int(f_obj.readline())
            self.row_targets = list(map(int, f_obj.readline().split()))
            self.col_targets = list(map(int, f_obj.readline().split()))
            self.grid = (self.n**2) * [0]

            fixed_list = f_obj.readlines()
            for line in fixed_list:
                x, y, val = map(int, line.split())
                self.grid[self.xytoi(x, y)] = val

            self.fixed = [val != 0 for val in self.grid]

    def print_all(self):
        """Print all state variables for debugging purposes."""
        print(f"n == {self.n}")
        print(f"row_targets == {self.row_targets}")
        print(f"col_targets == {self.col_targets}")
        print(f"grid == {self.grid}")
        print(f"fixed elts == {self.fixed}")

    def xytoi(self, x, y):
        """Take x,y from 0-(n-1) and return an index."""
        return self.n * x + y

    def itoxy(self, i):
        """Take i from 0, n^2 - 1 and return its xy pos."""
        x = i // self.n
        y = i - self.n * x
        return x, y


if __name__ == "__main__":
    K = Kubok("puzzle_files/example1.txt")
    K.print_all()
