import networkx as nx
import matplotlib.pyplot as plt

with open('ctx.txt', 'r') as file:
    lines = file.readlines()

graph = nx.DiGraph()

prev_grammar = []

i = 0

locked = False

ltc = ""

first_iteration = True
for line in lines:
    line = line.strip().split('|')
    grammar = line[0].strip()

    if not grammar:
        continue

    grammar_elements = grammar.split()
    grammar_elements.pop(0)

    print("----")
    print("Previous Grammar: ", prev_grammar)
    print("Current Grammar:", grammar_elements)


    for ge in grammar_elements:
    #    graph.add_node(f"{ge}_{i}")
       print(f"Adding node {ge}_{i}")

    if len(prev_grammar) == 1:
        i = i + 1

    if not prev_grammar:
        prev_grammar = grammar_elements
        continue

    to_connect = []
    # Check which element is missing from the previous grammar
    for ge in grammar_elements:
        if ge not in prev_grammar:
            to_connect.append(ge)

    try: 
        graph.remove_node("E_0")    
    except:
        pass

    print("To Connect: ", to_connect)

    if first_iteration:
        for ge in to_connect:
            graph.add_edge(f"{prev_grammar[0]}_{i}", f"{ge}_{i}")
        first_iteration = False
        prev_grammar = grammar_elements
        continue

    tt_connect = ""    
    for prev_ge in prev_grammar:
        if prev_ge not in grammar_elements:
            tt_connect = prev_ge

    flag = False
    if tt_connect == "":
        tt_connect = ltc
        flag = True
    ltc = tt_connect

    # wtf is this 
    hidden_index = 0
    if flag and len(to_connect) == 0:
        hidden_index = -1

    if tt_connect == "":
        locked = True
        tt_connect = 
        # tt_connect = f"{grammar_elements[-len(to_connect)]}"
        print("TT CONNECT NN: ", tt_connect)
        pass
        # print("EMPTY CONNECT DETECTED; ASIGNING FIRST ELEMENT")
        # tt_connect = prev_grammar[0]
        # to_connect = grammar_elements
    else:
        locked = False

    # Connecting the missing element from the previous grammar to the current grammar
    for ge in to_connect:
        graph.add_edge(f"{tt_connect}_{i+hidden_index}", f"{ge}_{i}")
        print(f"Connecting {tt_connect}_{i} to {ge}_{i}")


    print("To connect: ", tt_connect)
    prev_grammar = grammar_elements



# Draw the graph
pos = nx.drawing.nx_agraph.graphviz_layout(graph, prog='dot')
nx.draw(graph, pos, with_labels=True, node_size=500, font_size=10, node_color='lightblue')
plt.axis('off')
plt.show()
