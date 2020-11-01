# An alternative to assingment_10_2.py


for line in handle:
  if len(line) > 5 and line.startswith('From '):
    words = line.split()
    hours = words[5]
    hour = hours.split(':')
    h = hour[0]
    counts[h] = counts.get(h, 0) + 1
tmp = list()
for k,v in counts.items():
  new_v=(k,v)  
  tmp.append(new_v)
tmp = sorted(tmp, reverse = False)
for k,v in tmp[:]:
  print(k,v)
