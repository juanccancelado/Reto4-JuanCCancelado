from DataStructures.Graph import digraph as gr
from DataStructures.Graph import dijsktra_structure as ds

def test():

    grafo = gr.new_graph(5)
    gr.insert_vertex(grafo, "1", "A")
    gr.insert_vertex(grafo, "2", "B")
    gr.insert_vertex(grafo, "3", "C")
    gr.insert_vertex(grafo, "4", "D")
    gr.insert_vertex(grafo, "5", "E")

    gr.add_edge(grafo, "1", "2", 1)
    gr.add_edge(grafo, "1", "3", 2)
    gr.add_edge(grafo, "2", "3", 1)
    gr.add_edge(grafo, "2", "4", 3)
    gr.add_edge(grafo, "3", "4", 1)
    gr.add_edge(grafo, "4", "5", 1)
    gr.add_edge(grafo, "3", "5", 2)
    gr.add_edge(grafo, "1", "5", 4)
    gr.add_edge(grafo, "2", "5", 2)
    gr.add_edge(grafo, "3", "2", 1)


    print(ds.dijsktra(grafo, "1"))

    

    pass