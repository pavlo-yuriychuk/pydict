__author__ = 'pavlo'
from combinations import Combinations


def main():
    print Combinations(["a", "b", "ab", "abc"]).find_possible_combinations("aabcd")
    print Combinations(["a", "b", "ab", "abc"]).find_possible_combinations("aabc")

if __name__ == "__main__":
    main()
