def check_pal(s):
    n = len(s)
    for i in range(n//2):
        if (s[i] != s[n-1-i]):
            return False

    return True

print(check_pal("aabbaa"))

import random

edges = []
possible_edges = []
num_nodes = 0
num_edges = 0
is_directed = False
is_dag = False
is_weighted = False

def get_and_remove_random_edge():
    idx = random.randint(0, len(possible_edges)-1)
    edge = possible_edges[idx]
    del possible_edges[idx]  
    return edge

def output_test_case():
    file.write(f"{num_nodes} {num_edges}")
    file.write("\n")

    for i in range(num_edges):
        file.write(f"{edges[i]['v1']} {edges[i]['v2']}" + (f" {edges[i]['w']}" if is_weighted else ""))
        file.write("\n")

def generate_graph():
    global edges, possible_edges, num_nodes, num_edges, is_directed, is_weighted

    num_nodes = 100 #int(input("Enter the number of nodes: "))
    num_edges =  1000 #int(input("Enter the number of edges: "))

    start = 1

    is_directed = False
    is_weighted = True

    if is_directed:
        max_edges = num_nodes * (num_nodes - 1)
    else:
        max_edges = num_nodes * (num_nodes - 1) // 2

    if num_edges > max_edges:
        num_edges = max_edges
        print(f'Maximum number of edges connecting {num_nodes} nodes is {num_edges}!')

    edges = []
    possible_edges = []
    min_weight = 1
    max_weight = 100
    for i in range(num_nodes):
        for j in range(i + 1, num_nodes):
            v1 = i + start
            v2 = j + start
            w1 = None
            w2 = None
            if is_weighted:
                w1 = random.randint(min_weight, max_weight)
                w2 = random.randint(min_weight, max_weight)
            possible_edges.append({'v1': v1, 'v2': v2, 'w': w1})
            if is_directed:
                possible_edges.append({'v1': v2, 'v2': v1, 'w': w2})
    for i in range(num_edges):
        edge = get_and_remove_random_edge()
        edges.append(edge)
    output_test_case()


def generate_tree():
    n =  100000 #int(input("Enter the number of nodes: "))
    file.write(f"{n} {n-1}\n")
    for i in range(2, n + 1):
        a = i
        b = random.randint(1, i - 1)
        w = random.randint(1, 100)
        file.write(f"{a}" + f" {b}" + f" {w}")
        file.write("\n")

