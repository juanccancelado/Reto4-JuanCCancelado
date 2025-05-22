from DataStructures.Map import map_linear_probing as mp
from DataStructures.Priority_queue import priority_queue as pq
from DataStructures.Graph import digraph as gr

def new_dijsktra_structure(source, g_order):
    """ 

    Crea una estructura de busqueda usada en el algoritmo **dijsktra**.

    Se crea una estructura de busqueda con los siguientes atributos:

    - **source**: Vertice de origen. Se inicializa en ``source``
    - **visited**: Mapa con los vertices visitados. Se inicializa en ``None``
    - **pq**: Cola indexada con los vertices visitados. Se inicializa en ``None``

    :returns: Estructura de busqueda
    :rtype: dijsktra_search
    """
    structure = {
        "source": source,
        "visited": mp.new_map(
            g_order, 0.5),
        "pq": pq.new_heap()}
    return structure

def dijsktra(my_graph, source):
    """
    Implementa el algoritmo de **dijsktra** para encontrar el camino mas corto
    desde un vertice de origen a todos los demas vertices del grafo.

    :param my_graph: Grafo a recorrer
    :type my_graph: Graph
    :param source: Vertice de origen
    :type source: str
    :returns: Estructura de busqueda
    :rtype: dijsktra_search
    """
    g_order = gr.order(my_graph)
    structure = new_dijsktra_structure(source, g_order)
    visited = structure["visited"]
    pq_heap = structure["pq"]

    for v in gr.vertices(my_graph):
        mp.put(visited, v, float('inf'))
    mp.put(visited, source, 0)
    pq.insert(pq_heap, (0, source), source)  # (dist, vertex, key)

    while not pq.is_empty(pq_heap):
        current, vertex  = pq.remove_min(pq_heap)

        





        current_dist, u = pq.get_first_priority(pq_heap)
    
        if current_dist > mp.get(visited, u):
    
            for v in gr.adjacents(my_graph, u)["elements"]:
                edge = gr.get_edge(my_graph, u, v)
                weight = edge["weight"] if isinstance(edge, dict) else edge
                dist = mp.get(visited, u) + weight
                if dist < mp.get(visited, v):
                    mp.put(visited, v, dist)
                    pq.insert(pq_heap, (dist, v), v)

    return structure #["visited"] 

#for v in gr.vertices(graph):
#     print(f"A -> {v}: {visited['table'][v]['value']}")