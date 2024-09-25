import unittest
from BFS import BFS

class TestBFS(unittest.TestCase):

    def test_single_tree(self):
        # A basic connected graph
        adjacency_list = {
            'A': ['B', 'C'],
            'B': ['C', 'D'],
            'C': ['D'],
            'D': []
        }
        bfs = BFS(adjacency_list)
        result = bfs.run('A')
        expected_result = {
            'A': 0,
            'B': 1,
            'C': 1,
            'D': 2
        }
        self.assertEqual(result, expected_result)

    def test_disconnected_graph(self):
        # A disconnected graph where 'A' and 'B' are in one component, 'C' and 'D' in another
        adjacency_list = {
            'A': ['B'],
            'B': [],
            'C': ['D'],
            'D': []
        }
        bfs = BFS(adjacency_list)
        result_from_A = bfs.run('A')
        expected_result_from_A = {
            'A': 0,
            'B': 1
        }
        result_from_C = bfs.run('C')
        expected_result_from_C = {
            'C': 0,
            'D': 1
        }
        self.assertEqual(result_from_A, expected_result_from_A)
        self.assertEqual(result_from_C, expected_result_from_C)

    def test_cycle_graph(self):
        # A graph with a cycle A -> B -> C -> A
        adjacency_list = {
            'A': ['B'],
            'B': ['C'],
            'C': ['A']
        }
        bfs = BFS(adjacency_list)
        result = bfs.run('A')
        expected_result = {
            'A': 0,
            'B': 1,
            'C': 2
        }
        self.assertEqual(result, expected_result)

    def test_empty_graph(self):
        # An empty graph
        adjacency_list = {}
        bfs = BFS(adjacency_list)
        result = bfs.run('A')
        expected_result = {
            'A': 0
        }
        self.assertEqual(result, expected_result)

    def test_single_node_graph(self):
        # A graph with a single node and no edges
        adjacency_list = {
            'A': []
        }
        bfs = BFS(adjacency_list)
        result = bfs.run('A')
        expected_result = {
            'A': 0
        }
        self.assertEqual(result, expected_result)

    def test_no_edges(self):
        # A graph where no nodes have any outgoing edges
        adjacency_list = {
            'A': [],
            'B': [],
            'C': []
        }
        bfs = BFS(adjacency_list)
        result = bfs.run('A')
        expected_result = {
            'A': 0
        }
        self.assertEqual(result, expected_result)

    def test_non_existent_start_node(self):
        # Start node is not in the adjacency list
        adjacency_list = {
            'A': ['B'],
            'B': ['C'],
            'C': []
        }
        bfs = BFS(adjacency_list)
        result = bfs.run('Z')
        expected_result = {
            'Z': 0  # If the start node is non-existent, it should just return that node with distance 0
        }
        self.assertEqual(result, expected_result)

if __name__ == "__main__":
    unittest.main()
