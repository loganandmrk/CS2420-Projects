from graph import Graph

def main():
    G = Graph()
    vA = Graph.Vertex("A")
    vB = Graph.Vertex("B")
    vC = Graph.Vertex("C")
    vD = Graph.Vertex("D")
    vE = Graph.Vertex("E")
    vF = Graph.Vertex("F")
    print(G.Vertex("A").label)

    G.add_vertex(vA)
    G.add_vertex(vB)
    G.add_vertex(vC)
    G.add_vertex(vD)
    G.add_vertex(vE)
    G.add_vertex(vF)

    G.add_edge(vA, vB, 2)
    print(G.adjacency_list)
    G.add_edge(vA, vF, 9)
    G.add_edge(vB, vC, 8)
    G.add_edge(vB, vD, 15)
    G.add_edge(vB, vF, 6)
    G.add_edge(vC, vD, 1)
    G.add_edge(vE, vC, 7)
    G.add_edge(vE, vD, 3)
    G.add_edge(vF, vB, 6)
    G.add_edge(vF, vE, 3)

    print("starting BFS with vertex A")
    for vertex in G.bfs("A"):
        print(vertex, end = "")
    print()

if __name__ == "__main__":
    main()