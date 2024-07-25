import networkx as nx
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import heapq

def visualize_dijkstra(graph, start_node):
    node_colors = {node: 'blue' for node in graph.nodes()}
    node_distances = {node: float('inf') for node in graph.nodes()}
    edge_colors = {edge: 'black' for edge in graph.edges()}

    node_distances[start_node] = 0
    priority_queue = [(0, start_node)]

    fig, ax = plt.subplots(figsize=(10, 7))
    pos = nx.spring_layout(graph)

    def update(frame):
        if priority_queue:
            current_distance, current_node = heapq.heappop(priority_queue)
            if current_distance > node_distances[current_node]:
                return

            node_colors[current_node] = 'red'
            for neighbor in graph.neighbors(current_node):
                edge = (current_node, neighbor)
                edge_weight = graph[current_node][neighbor]['weight']
                distance = current_distance + edge_weight

                if distance < node_distances[neighbor]:
                    node_distances[neighbor] = distance
                    heapq.heappush(priority_queue, (distance, neighbor))
                    edge_colors[edge] = 'green'
                    edge_colors[(neighbor, current_node)] = 'green'

            node_colors[current_node] = 'green'

        ax.clear()
        nx.draw(graph, pos, ax=ax, node_color=[node_colors[node] for node in graph.nodes()],
                with_labels=True, node_size=1000, edge_color=[edge_colors[edge] for edge in graph.edges()],
                labels={node: f"{node}" for node in graph.nodes()})
        
        # Draw edge labels with weights
        edge_labels = {(u, v): f"{data['weight']}" for u, v, data in graph.edges(data=True)}
        nx.draw_networkx_edge_labels(graph, pos, edge_labels=edge_labels, ax=ax, font_color='red')

        # Display the array of shortest distances below the diagram
        distance_str = ' '.join(f"{node} : {dist if dist != float('inf') else '∞'}," for node, dist in node_distances.items())
        ax.text(0.5, -0.1, f"Shortest Distances: {distance_str}", horizontalalignment='center', fontsize=12, color='black', transform=ax.transAxes)
        
        ax.set_title(f"Priority Queue: {priority_queue}")

    ani = FuncAnimation(fig, update, frames=range(len(graph.nodes()) * 2), repeat=False, interval=1000)
    plt.show()

# Create a graph with weighted edges
G = nx.Graph()
edges = [
    (0, 1, 4), (0, 2, 1), (0, 3, 7), (1, 4, 2), (1, 5, 3),
    (2, 6, 5), (2, 7, 6), (3, 7, 8), (3, 8, 4), (4, 9, 1),
    (4, 6, 6), (5, 9, 3), (5, 7, 2), (6, 8, 7), (6, 9, 4),
    (7, 8, 3), (8, 9, 5), (0, 4, 6), (1, 7, 8), (2, 5, 4),
    (3, 6, 5), (4, 8, 3), (5, 6, 1)
]

G.add_weighted_edges_from(edges)

# Dijkstra's algorithm with source node 0
visualize_dijkstra(G, 0)
