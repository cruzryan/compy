import networkx as nx
import matplotlib.pyplot as plt

def generate_derivation_graph(stack):
    graph = nx.DiGraph()
    stack = stack.strip().split("\n")

    node_index = {}
    index = 1
    
    for line in stack:
        line = line.strip()
        if line:
            lhs, _ = line.split("|")
            lhs = lhs.strip()

            if lhs == "$":
                continue

            terms = lhs.split(" ")
            for term in terms:
                if term not in node_index:
                    node_index[term] = index
                    index += 1
                node_label = f"{term}_{node_index[term]}"
                graph.add_node(node_label)

    for i in range(len(stack) - 1):
        line = stack[i].strip()
        if line:
            lhs, _ = line.split("|")
            lhs = lhs.strip()

            if lhs == "$":
                continue

            next_line = stack[i + 1].strip()
            if next_line:
                next_lhs, _ = next_line.split("|")
                next_lhs = next_lhs.strip()

                if next_lhs == "$":
                    continue

                terms = lhs.split(" ")
                next_terms = next_lhs.split(" ")

                for j in range(min(len(terms), len(next_terms))):
                    term = terms[j]
                    next_term = next_terms[j]

                    if term in node_index:
                        term_index = node_index[term]
                        term_label = f"{term}_{term_index}"
                    else:
                        term_label = term

                    if next_term in node_index:
                        next_term_index = node_index[next_term]
                        next_term_label = f"{next_term}_{next_term_index}"
                    else:
                        next_term_label = next_term

                    graph.add_edge(term_label, next_term_label)

    plt.figure(figsize=(8, 6))
    pos = nx.spring_layout(graph)
    nx.draw_networkx(graph, pos, with_labels=True, node_size=500, font_size=12, node_color='lightblue', edge_color='gray')
    plt.title("LL1 Derivation Graph")
    plt.axis('off')
    plt.show()

# Example usage:
stack = """
$ E | 1+2*3$
$ Ep T | 1+2*3$
$ Ep Tp F | 1+2*3$
$ Ep Tp num | 1+2*3$
$ Ep Tp | +2*3$
$ Ep | +2*3$
$ Ep T mas | +2*3$
$ Ep T | 2*3$
$ Ep Tp F | 2*3$
$ Ep Tp num | 2*3$
$ Ep Tp | *3$
$ Ep Tp F por | *3$
$ Ep Tp F | 3$
$ Ep Tp num | 3$
$ Ep Tp | $
$ Ep | $
$ | $
"""

generate_derivation_graph(stack)
