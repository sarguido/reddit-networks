# Formatting the data.
# DON'T RUN THIS.

import json
import itertools
import pickle
import csv

f = json.load(open('../data/redd0t.json'))
subreddits = {}

for sub in f:
	if sub['sub_name']:
		name = sub['sub_name']
		subreddits[name] = sub['sub_posters'].keys(), sub['sub_commenters'].keys()
		subreddits[name] = set([item for sublist in subreddits[name] for item in sublist])

f2 = open('subslist.p', 'wb')
subnames = subreddits.keys()
sub_perms = itertools.permutations(subnames, 2)

biglist = []

for item in sub_perms:
	biglist.append(list(item))

for item in biglist:
	item.sort()

unique_perms = []

for item in biglist:
	if item not in unique_perms:
		unique_perms.append(item)
		print item

pickle.dump(unique_perms, f2)


itemlist = pickle.load(open('subslist.p', 'rb'))

with open('weights.csv', 'wb') as csvfile:
	csv_write = csv.writer(csvfile)
	for item in itemlist:
		weight = 0
		for p in subreddits[item[0]]:
			if p in subreddits[item[1]]:
				weight += 1
		csv_write.writerow([item[0], item[1], weight])
		print item[0], item[1], weight
