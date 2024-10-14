from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Enable CORS

def dijkstra(graph, start):
    shortest_paths = {node: float('inf') for node in graph}
    shortest_paths[start] = 0
    visited = set()

    while len(visited) < len(graph):
        min_node = None
        for node in graph:
            if node not in visited:
                if min_node is None or shortest_paths[node] < shortest_paths[min_node]:
                    min_node = node

        for neighbor, weight in graph[min_node].items():
            new_distance = shortest_paths[min_node] + weight
            if new_distance < shortest_paths[neighbor]:
                shortest_paths[neighbor] = new_distance
        
        visited.add(min_node)

    return shortest_paths

@app.route('/dijkstra', methods=['POST'])
def dijkstra_api():
    data = request.get_json()
    graph = data['graph']
    start = data['start']
    result = dijkstra(graph, start)
    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True)
