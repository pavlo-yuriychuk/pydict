class NumberComposition:
    def __init__(self, value):
        self.value = value

    def __iter__(self):
        if self.value == 0:
            yield [0]
        elif self.value == 1:
            yield [1]
        elif self.value == 2:
            yield [2]
            yield [1, 1]
        else:
            for items_count in range(2, self.value + 1):
                for combination in self.find_all_combinations(items_count, self.value):
                    if sum(combination) == self.value:
                        yield combination

    @staticmethod
    def find_all_combinations(count, max_value):
        def add_one(accum_value, x):
            values, accum = accum_value
            x += accum
            accum = 1 if x >= max_value else 0
            values.append(x % max_value)
            return values, accum

        current = [0 for i in range(count)]
        yield map(lambda x: x + 1, current)
        for i in range(max_value ** count):
            next = reduce(add_one, current, ([], 1))
            current = next[0]
            yield map(lambda x: x + 1, current)


class Dictionary:
    def __init__(self, words):
        self.words = set(words)

    def has(self, value):
        return value in self.words


class Combinations:
    def __init__(self, dictionary):
        self.dictionary = Dictionary(dictionary)

    @staticmethod
    def split_string(string, composition):
        result = []
        index = 0
        for item in composition:
            result.append(string[index:index + item])
            index += item
        return result

    def find_possible_combinations(self, string):
        if len(string) == 0:
            return []
        else:
            result = []
            for composition in NumberComposition(len(string)):
                sub_strings = self.split_string(string, composition)
                if set(sub_strings).issubset(self.dictionary.words):
                    result.append(" ".join(sub_strings))
            return result


if __name__ == "__main__":
    assert Combinations(["a", "b", "ab", "abc"]).find_possible_combinations("aabcd") == []
    assert Combinations(["a", "b", "ab", "abc"]).find_possible_combinations("aabc") == ['a abc']