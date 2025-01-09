
import random

NUM_NODES = 0
NUM_EDGES = 0
IS_DIRECTED = False
IS_DAG = False
IS_WEIGHTED = False

def check_pal(s):
   
    n = len(s)
    for i in range(n // 2):
        if s[i] != s[n - 1 - i]:
            return False
    return True

def get_and_remove_random_edge():
   
    idx = random.randint(0, len(possible_edges) - 1)
    edge = possible_edges[idx]
    del possible_edges[idx]
    return edge

def output_test_case(file):
   
    file.write(f"{NUM_NODES} {NUM_EDGES}\n")
    for i in range(NUM_EDGES):
        file.write(f"{edges[i]['v1']} {edges[i]['v2']}" + 
                  (f" {edges[i]['w']}" if IS_WEIGHTED else ""))
        file.write("\n")

def generate_graph(file):
   
    global edges, possible_edges, NUM_NODES, NUM_EDGES, IS_DIRECTED, IS_WEIGHTED
    NUM_NODES = 100
    NUM_EDGES = 1000
    start = 1
    IS_DIRECTED = False
    IS_WEIGHTED = True
    
    if IS_DIRECTED:
        max_edges = NUM_NODES * (NUM_NODES - 1)
    else:
        max_edges = NUM_NODES * (NUM_NODES - 1) // 2
        
    if NUM_EDGES > max_edges:
        NUM_EDGES = max_edges
        print(f'Maximum number of edges connecting {NUM_NODES} nodes is {NUM_EDGES}!')
        
    edges = []
    possible_edges = []
    min_weight = 1
    max_weight = 100
    
    for i in range(NUM_NODES):
        for j in range(i + 1, NUM_NODES):
            v1 = i + start
            v2 = j + start
            w1 = None
            w2 = None
            if IS_WEIGHTED:
                w1 = random.randint(min_weight, max_weight)
                w2 = random.randint(min_weight, max_weight)
            possible_edges.append({'v1': v1, 'v2': v2, 'w': w1})
            if IS_DIRECTED:
                possible_edges.append({'v1': v2, 'v2': v1, 'w': w2})
                
    for i in range(NUM_EDGES):
        edge = get_and_remove_random_edge()
        edges.append(edge)
        
    output_test_case(file)

def generate_tree(file):
   
    n = 100000
    file.write(f"{n} {n - 1}\n")
    for i in range(2, n + 1):
        a = i
        b = random.randint(1, i - 1)
        w = random.randint(1, 100)
        file.write(f"{a} {b} {w}\n")
