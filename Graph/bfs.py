import networkx as nx
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from collections import deque

# Time complexity: O(V + E)
# Space complexity: O(V)

def visualize_bfs(graph, start_node):
    node_colors = {node: 'blue' for node in graph.nodes()}
    queue = deque([start_node])
    visited = set()
    node_labels = {node: node for node in graph.nodes()}
    
    fig, ax = plt.subplots(figsize=(10, 7))
    pos = nx.spring_layout(graph)
    
    def update(frame):
        if queue:
            current_node = queue.popleft()
            if current_node not in visited:
                visited.add(current_node)
                node_colors[current_node] = 'red'
                node_labels[current_node] = str(node_labels[current_node]) + '*'
                
                for neighbor in graph.neighbors(current_node):
                    if neighbor not in visited and neighbor not in queue:
                        queue.append(neighbor)
                
                node_colors[current_node] = 'green'
                
        ax.clear()
        nx.draw(graph, pos, ax=ax, node_color=[node_colors[node] for node in graph.nodes()], 
                labels=node_labels, with_labels=True, node_size=500)
        ax.set_title(f"Queue: {list(queue)}")
    
    ani = FuncAnimation(fig, update, frames=range(len(graph.nodes()) * 2), repeat=False, interval=1000)
    plt.show()

G = nx.Graph()
edges = [
    (0, 1), (0, 2), (1, 3), (1, 4), (2, 5), (2, 6),
    (3, 7), (3, 8), (4, 9), (4, 10), (5, 11), (5, 12),
    (6, 13), (6, 14), (7, 15), (7, 16), (8, 17), (8, 18),
    (9, 19), (9, 20), (10, 21), (10, 22), (11, 23), (11, 24),
    (12, 25), (12, 26), (13, 27), (13, 28), (14, 29), (14, 30),
    (15, 31), (15, 32), (16, 33), (16, 34), (17, 35), (17, 36),
    (18, 37), (18, 38), (19, 39), (19, 40), (20, 41), (20, 42),
    (21, 43), (21, 44), (22, 45), (22, 46), (23, 47), (23, 48),
    (24, 49), (25, 26), (27, 28), (29, 30), (31, 32), (33, 34),
    (35, 36), (37, 38), (39, 40), (41, 42), (43, 44), (45, 46),
    (47, 48), (48, 49)
]

G.add_edges_from(edges)

visualize_bfs(G, 0)
