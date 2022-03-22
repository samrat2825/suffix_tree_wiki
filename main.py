from modules.wikipedia import *
from modules.suffix_tree import *

print("\n\nEnter Wikipedia URL to index")
url = input()

print("\nFetching Data....")
raw_text = fetchData(url)
text = raw_text.split('.')

print("Data Fetched \n Building Suffix Tree...")
# buildTree(raw_text)

# print("Tree construction completed\n")
# print("Enter pattern to search")
# pattern = input()

# occurences = find_all(pattern)
# print(occurences)
