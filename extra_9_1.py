# using dictionaries to count words in a file 

name = input('Enter file name ')
handle = open(name)

counts = dict()


for line in handle:
  words = line.split()
  for word in words:
    counts[word] = counts.get(word, 0) + 1
bigcount = None
bigword = None 
print(counts)
for k,v in counts.items():
  if bigcount == None or v > bigcount:
    bigword = k
    bigcount = v
print('The most common word was *', bigword, '* appearing', bigcount,'times in the file', name)
