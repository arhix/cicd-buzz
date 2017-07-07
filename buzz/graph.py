import secrets
import itertools


def generate_graph(count_points=10, count_edges=10):
    graph = {"nodes": [], "edges": []}
    cells = generate_plane(count_points)
    points = list(range(0, count_points))
    edges = list(range(0, count_edges))
    for point in points:
        cell = secrets.choice(cells)
        cells.remove(cell)
        graph["nodes"].append(generate_point(point, cell))
    graph["edges"] = [generate_random_edge(edge, points) for edge in edges]
    return graph


def generate_point(point_id, cell):
    return {
        "id": "n%d" % point_id,
        "label": "n%d" % point_id,
        "x": cell['x'],
        "y": cell['y'],
        "size": 1,
    }


def generate_plane(count_points):
    cells = itertools.product(range(0, count_points), repeat=2)
    return [{'x': x, 'y': y} for x, y in cells]


def generate_random_edge(edge_id, points):
    return {
        "id": "e%d" % edge_id,
        "source": "n%d" % secrets.choice(points),
        "target": "n%d" % secrets.choice(points),
    }
