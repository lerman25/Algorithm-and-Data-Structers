import unittest
from DFS import DFS
class TestDFS(unittest.TestCase):

    def test_single_tree(self):
        adjacency_list = {
            'A': ['B', 'C'],
            'B': ['C'],
            'C': ['D'],
            'D': []
        }
        dfs = DFS(adjacency_list)
        result = dfs.run('A')
        expected_result = [
            [('D', 4, 5), ('C', 3, 6), ('B', 2, 7), ('A', 1, 8)]
        ]
        self.assertEqual(result, expected_result)

    def test_disconnected_graph(self):
        adjacency_list = {
            'A': ['B'],
            'B': [],
            'C': ['D'],
            'D': []
        }
        dfs = DFS(adjacency_list)
        result = dfs.run()
        expected_result = [
            [('B', 2, 3), ('A', 1, 4)],
            [('D', 6, 7), ('C', 5, 8)]
        ]
        self.assertEqual(result, expected_result)

    def test_cycle_graph(self):
        adjacency_list = {
            'A': ['B'],
            'B': ['C'],
            'C': ['A']
        }
        dfs = DFS(adjacency_list)
        result = dfs.run('A')
        expected_result = [
            [('C', 3, 4), ('B', 2, 5), ('A', 1, 6)]
        ]
        self.assertEqual(result, expected_result)

    def test_empty_graph(self):
        adjacency_list = {}
        dfs = DFS(adjacency_list)
        result = dfs.run()
        expected_result = []
        self.assertEqual(result, expected_result)

    def test_single_node_graph(self):
        adjacency_list = {
            'A': []
        }
        dfs = DFS(adjacency_list)
        result = dfs.run('A')
        expected_result = [
            [('A', 1, 2)]
        ]
        self.assertEqual(result, expected_result)

    def test_no_start_node(self):
        adjacency_list = {
            'A': ['B'],
            'B': ['C'],
            'C': []
        }
        dfs = DFS(adjacency_list)
        result = dfs.run()  # No start node provided
        expected_result = [
            [('C', 3, 4), ('B', 2, 5), ('A', 1, 6)]
        ]
        self.assertEqual(result, expected_result)

if __name__ == "__main__":
    unittest.main()
