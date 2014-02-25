
def find_subranges(n, m):
	if n == 0 or m > n or m == 0:
		return None
	elif n == 1:
		return [(0, 0)]
	elif n == m:
		return [(0, n)]
	else:
		return map(lambda x: (x, x + m), range(n - m))

def find_all_subranges(n):
	if n == 0:
		return None
	elif n == 1:
		return find_subranges(1, 1)
	elif n == 2:
		return find_subranges(2, 2) + find_subranges(2, 1)
	else:
		result = []
		for i in range(1, n + 1):
			result += find_subranges(n, i)
		return result

class Dictionary:

	def __init__(self, words):
		self.words = frozenset(words)

	def has(self, value):
		return value in self.words


class Combinations:

	def __init__(self, dictionary):
		self.dictionary = dictionary

	def find_possible_combinations(self, string):
		if len(string) == 0:
			return []
		else:
			result = []
			used = set()
			subranges = find_all_subranges(len(string))
			for subrange in subranges:
				substring = string[subrange[0]:subrange[1]]
				print substring
				if self.dictionary.has(substring):
					used.append(substring)
					result.append(substring)
				else:
					if not substring in used:
						result = []
			return result

if __name__ == "__main__":
	assert Combinations(Dictionary(["a", "b", "ab", "abc"])).find_possible_combinations("aabcd") == []
	print Combinations(Dictionary(["a", "b", "ab", "abc"])).find_possible_combinations("aabc")