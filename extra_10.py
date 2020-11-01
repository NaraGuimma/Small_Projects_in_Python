# Show the top 10 most common word in a file

fname = input('Enter file name: ')
handle = open(fname)
counts = dict()

for line in handle:
  words = line.split()
  for word in words:
    counts[word] = counts.get(word, 0) +1
tmp = list()
for k,v in counts.items():
  tmp.append((v,k))
tmp=sorted(tmp, reverse = True)
for v,k in tmp[:10]:
  print(k,v)
