# Solo para probar

import networkx as nx
import matplotlib.pyplot as plt

with open('ctx.txt', 'r') as file:
    lines = file.readlines()

graph = nx.DiGraph()

graph.add_edge("E_1", "Ep_1")
graph.add_edge("E_1", "T_1")
graph.add_edge("T_1", "F_1")
graph.add_edge("F_1", "num_1")

graph.add_edge("T_1", "Tp_1")

graph.add_edge("Tp_1", "mas_1")
graph.add_edge("Tp_1", "T_2")
graph.add_edge("Tp_1", "Ep_2")

graph.add_edge("T_2", "F_2")
graph.add_edge("F_2", "num_2")
graph.add_edge("T_2", "Tp_3")

graph.add_edge("Tp_3", "Tp_4")
graph.add_edge("Tp_3", "por_1")
graph.add_edge("Tp_3", "F_3")

graph.add_edge("F_3", "num_3")


def shg():
    with open('ctx.txt', 'r') as file:
        l = file.readlines()
        if "$ E | 1+2*3$" not in l[0]:
            return
    pos = nx.drawing.nx_agraph.graphviz_layout(graph, prog='dot')
    nx.draw(graph, pos, with_labels=True, node_size=500, font_size=10, node_color='lightblue')
    plt.axis('off')
    plt.show()
