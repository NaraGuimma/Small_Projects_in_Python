# rite a program to read through the mbox-short.txt and figure out the distribution by hour of the day for each of the messages. You can pull the hour out from the 'From ' line by finding the time and then splitting the string a second time using a colon.
# From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008
# Once you have accumulated the counts for each hour, print out the counts, sorted by hour as shown below.


counts = dict()
name = input("Enter file: ")
if len(name) < 1 : name = "test.txt"
handle = open(name)
for line in handle:
  if len(line) > 5 and line.startswith('From '):
    words = line.split()
    hours = words[5]
    hour = hours.split(':')
    h = hour[0]
    counts[h] = counts.get(h, 0) + 1

#print(counts)   
tmp = list()
for k,v in counts.items():
  tmp.append((v,k))
tmp.sort(reverse = True)
for v,k in tmp:
  print(k,v)
