from collections import Counter
import re

# inp = input("Enter a line:")
# print(len(inp.split()))
path = 'A good man is hard to fin.txt'
words = re.findall('\w+', open(path, encoding='UTF-8').read().lower())
print(Counter(words).most_common(10))

