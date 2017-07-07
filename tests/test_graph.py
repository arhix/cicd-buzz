from buzz import graph


def test_generate_graph():
    count_points, count_edges = 8, 6
    graph_data = graph.generate_graph(count_points, count_edges)
    assert isinstance(graph_data, dict)
    assert len(graph_data['nodes']) == count_points
    assert len(graph_data['edges']) == count_edges


def test_generate_point():
    point_data = graph.generate_point(99, {'x': 7, 'y': 3})
    assert isinstance(point_data, dict)
    assert all(k in point_data.keys() for k in ('id', 'x', 'y', 'size'))


def test_generate_plane():
    size = 8
    point_data = graph.generate_plane(size)
    assert isinstance(point_data, list)
    assert len(point_data) == size * size
    assert all(k in point_data[0].keys() for k in ('x', 'y'))


def test_generate_random_edge():
    point_data = graph.generate_random_edge(77, [11, 66])
    assert isinstance(point_data, dict)
    assert all(k in point_data.keys() for k in ('id', 'source', 'target'))
