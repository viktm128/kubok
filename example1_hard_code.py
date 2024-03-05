"""Brute-force solver for first Kubok ever found."""

from itertools import permutations


def check(perm):
    """Check sum conditions for successful answer."""
    return not (
        sum(perm[0:3]) + 15 != 50 or
        sum(perm[3:6]) + 9 != 21 or
        sum(perm[6:9]) + 7 != 43 or
        sum(perm[9:12]) + 4 != 22 or
        perm[0] + perm[3] + perm[6] + 4 != 29 or
        perm[1] + perm[4] + 7 + perm[9] != 34 or
        perm[2] + 9 + perm[7] + perm[10] != 36 or
        15 + perm[5] + perm[8] + perm[11] != 37
    )


def main():
    """Iterate through permutations of the remaining numbers."""
    nums = [1, 2, 3, 5, 6, 8, 10, 11, 12, 13, 14, 16]

    for perm in permutations(nums):
        if check(perm):
            print(perm)
            break


if __name__ == "__main__":
    main()
