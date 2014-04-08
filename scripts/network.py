# For creating networks!

import networkx as nx
import csv
import matplotlib.pyplot as plt

G = nx.Graph()

with open('../data/weights.csv', 'rb') as csvfile:
	reader = csv.reader(csvfile)
	for r in reader:
		if int(r[2]) >= 100:
			G.add_edge(r[0], r[1], weight=int(r[2]))

nx.draw(G)
plt.show()
#plt.savefig('../graphs/graph.pdf')

