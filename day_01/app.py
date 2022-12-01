import os
from base import Elve, Snack

with open(os.path.join('./day_01/data.txt')) as f:
    input_data = f.read().split('\n')

snacks = []
elves = []

for line in input_data:
    if line != '':
        snacks.append(Snack(line))
    else:
        elves.append(Elve(snacks))
        snacks = []

print(max(elves, key=lambda elve: elve.total_calories))

elves.sort(key=lambda elve: elve.total_calories, reverse=True)
print('Sum of total calories for top 3 elves: ' +
      str(sum(elve.total_calories for elve in elves[:3])))
