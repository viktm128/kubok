# Build a Kubok solver for an arbitrary n x n Kubok. 
# Ideally run algorithm analysis and verify performance with a test bench.


class Kubok:

    def __init__(self, f_name):

        f_obj = read(f_name, "r", encoding="utf-8")
        
        self.n = int(f_obj.readline())
        self.row_targets = self.n * [0]
        self.col_targets = self.n * [0]
        self.grid = (n**2) * [0]
        read_fixed_numbers()

    def xytoi(x, y):
        """Take x,y from 0-(n-1) and return an index."""

    def itoxy(i):
        """Take i from 0, n^2 - 1 and return its xy pos."""

    
    def read_fixed_numbers():
        """Find and store the positions of the fixed numbers."""

