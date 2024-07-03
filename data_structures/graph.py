import networkx as nx
import matplotlib.pyplot as plt

graph = nx.Graph()   # створення графа


graph.add_node("Vlad")
graph.add_node("Lena")
graph.add_node("OLeg")
graph.add_node("Luida")
graph.add_node("Alica")
graph.add_node("Pusha")

graph.add_edge("Vlad", "Lena")
graph.add_edge("OLeg", "Luida")
graph.add_edge("Vlad", "Luida")
graph.add_edge("Alica", "Pusha")
graph.add_edge("Luida", "Pusha")

nx.draw(graph, with_labels=True)
plt.show()







