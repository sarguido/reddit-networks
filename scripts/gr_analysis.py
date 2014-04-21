import networkx as nx
import csv

gender_edges = nx.Graph()

with open('../data/gender_edges.csv', 'rb') as f:
	reader = csv.reader(f)
	for r in reader:
		gender_edges.add_edge(r[0], r[1], weight=float(r[2]))

nx.draw(gender_edges)

# Average degree
degrees = nx.degree_centrality(gender_edges)
avg_degree = sum(degrees.values()) / len(degrees)

# Average closeness
closeness = nx.closeness_centrality(gender_edges)
avg_closeness = sum(closeness.values()) / len(closeness)

# Average betweenness
betweenness = nx.betweenness_centrality(gender_edges, weight='weight')
avg_betweenness = sum(betweenness.values()) / len(betweenness)

# Average clustering
avg_clustering = nx.average_clustering(gender_edges, weight='weight')

