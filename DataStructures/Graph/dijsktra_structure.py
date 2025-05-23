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
        "pq": pq.new_heap(),
        "predecessors": {}
        }
    return structure

def dijkstra(my_graph, source):
    
    if gr.order(my_graph) == 0:
        raise Exception("El grafo está vacío, no se puede ejecutar Dijkstra.")
    else:
        aux_structure = new_dijsktra_structure(source, gr.order(my_graph))
        pq.insert(aux_structure["pq"], source, 0)
        mp.put(aux_structure["visited"], source, 0)
        while not pq.is_empty(aux_structure["pq"]):
            vertex = pq.remove(aux_structure["pq"])
            # Get the adjacents of the current vertex as a list of dictionaries
            adjacents = mp.value_set(gr.adjacents(my_graph, vertex))
            # Iterate through each adjacent vertex
            for adj in adjacents["elements"]:
                neighbor = adj["to"]      # The adjacent vertex
                weight = adj["weight"]    # The weight of the edge to the neighbor

                # Check if the neighbor has been visited using the map's get function
                if mp.get(aux_structure["visited"], neighbor) is None:
                    # Calculate the new distance from the source to this neighbor
                    new_distance = weight + dist_to(vertex, aux_structure)
                    # If this path is shorter, or the neighbor hasn't been reached before
                    if (mp.get(aux_structure["visited"], neighbor) is None or
                        new_distance < dist_to(neighbor, aux_structure)):
                        # Insert the neighbor into the priority queue with the new distance
                        pq.insert(aux_structure["pq"], neighbor, new_distance)
                        # Update the visited map with the new shortest distance
                        mp.put(aux_structure["visited"], neighbor, new_distance)
                        # Set the predecessor for path reconstruction
                        aux_structure["predecessors"][neighbor] = vertex
        return aux_structure 
    
def dist_to(key_v, aux_structure):
    # Use the map's get function to retrieve the distance for key_v
    distance = mp.get(aux_structure["visited"], key_v)
    if distance is not None:
        return distance
    else:
        raise Exception("No existe una distancia registrada para el vértice dado.")
    
def has_path_to(key_v, aux_structure):

    if key_v in aux_structure["visited"]["elements"]:
        return True
    else:
        raise Exception("No existe un camino desde el vértice fuente hasta el vértice dado.")

def path_to(key_v, aux_structure):
    
    if not has_path_to(key_v, aux_structure):
        raise Exception("No existe un camino desde el vértice fuente hasta el vértice dado.")
    
    path = []
    current = key_v
    while current != aux_structure["source"]:
        path.append(current)
        current = aux_structure["predecessor"][current]
    path.append(aux_structure["source"])
    path.reverse()  
    return path