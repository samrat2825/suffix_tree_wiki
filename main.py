from modules.wikipedia import *
from modules.suffix_tree import *
from modules.helpers import *

print("\n\nEnter Wikipedia URL to index")
print("\nPress 1 if url = https://en.wikipedia.org/wiki/Synthetic_diamond;\nelse: Enter Url ")
url = input()
if url == '1':
    url = 'https://en.wikipedia.org/wiki/Synthetic_diamond'

print("\nFetching Data....")
raw_text = fetchData(url)
text = raw_text.split('.')

print("Data Fetched \nBuilding Index...")
index = []

for i in text:
    padding = 0
    if len(index) > 0:
        padding = index[-1]
    index.append(len(i)+int(padding))
# print(index)

print("Building Suffix Tree...")
# st = STree(raw_text)

# Generalized Suffix-Tree example.
st = STree(text)

print("\nTree construction completed\n")
print("Enter pattern to search")
# pattern = input()
pattern = "diamonds"

occurences = list(st.find_all(pattern))
occurences.sort()

print("Index of Occurences", occurences, len(occurences), "\n")

output = []
for occurence in occurences:
    pos = binarySearch(index, occurence)
    if pos >= 0 and pos < len(text):
        # if pos-1 >= 0 and pos+1 < len(text):
        #     print(occurence, index[pos], text[pos-1],
        #           "\n", text[pos], "\n", text[pos+1])
        # elif pos-1 >= 0:
        #     print(occurence, index[pos], text[pos-1], "\n", text[pos])
        # else:
        #     print(occurence, index[pos], text[pos], "\n", text[pos+1])
        output.append(text[pos])

# print(len(output))
print(output)
