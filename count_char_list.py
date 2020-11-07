import math

z = ['atoms', 4, 'automatic', 6, 'proton', 4, 'electron', 4, 'electron', 'atoms']

for i in range(len(z)):
    c = z[i]
    if isinstance(c, str):
      count = c.count('a')
      print(z[i], count)
    else:
      print('INTEGER')
