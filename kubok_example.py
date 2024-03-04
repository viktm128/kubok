from itertools import permutations


def check(perm):
    if sum(perm[0:3]) + 15 != 50:
        return False
    if sum(perm[3:6]) + 9 != 21:
        return False
    if sum(perm[6:9]) + 7 != 43:
        return False
    if sum(perm[9:12]) + 4 != 22:
        return False

    if perm[0] + perm[3] + perm[6] + 4 != 29:
        return False
    if perm[1] + perm[4] + 7 + perm[9] != 34:
        return False
    if perm[2] + 9 + perm[7] + perm[10] != 36:
        return False
    if 15 + perm[5] + perm[8] + perm[11] != 37:
        return False

    return True



def main():
    nums = [1, 2, 3, 5, 6, 8, 10, 11, 12, 13, 14, 16]

    for perm in permutations(nums):
        if check(perm):
            print(perm)
            break

if __name__ == "__main__":
    main()




