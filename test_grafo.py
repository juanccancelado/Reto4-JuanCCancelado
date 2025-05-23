from DataStructures.Graph import digraph as gr
from DataStructures.Graph import dijsktra_structure as ds
from DataStructures.Map import map_linear_probing as mp
from DataStructures.Priority_queue import priority_queue as pq

def test():

    grafo = gr.new_graph(5)
    gr.insert_vertex(grafo, "A", 1)
    gr.insert_vertex(grafo, "B", 2)
    gr.insert_vertex(grafo, "C", 3)

    gr.add_edge(grafo, "A", "B", 1)
    gr.add_edge(grafo, "A", "C", 2)
    gr.add_edge(grafo, "B", "C", 3)

    peque = pq.new_heap(compare)
    pq.insert(peque, 1)
    pq.insert(peque, 2)
    pq.insert(peque, 4)
    pq.insert(peque, 5)
    pq.insert(peque, 8)
    pq.insert(peque, 10)
    pq.insert(peque, 15)
    
    print(peque)
    print(pq.remove(peque))

    pass

def compare(a, b):
    if a == b:
        return 0
    elif a < b:
        return -1
    else:
        return 1