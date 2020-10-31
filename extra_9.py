# Building a dictionary to count words typed in. Using the concept of dictionaries to build in a counter 

counts = dict()
print('WRITE SOME TEXT')
line = input('')
line = line.lower()
words = line.split()
for word in words:
  counts[word] = counts.get(word, 0) + 1 

sorted_counts = sorted(counts.items(), key=lambda x: x[1]) 

print(counts)
