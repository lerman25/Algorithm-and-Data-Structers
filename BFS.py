import collections

class BFS:
    def __init__(self,adj_list):
        self.adj_list = adj_list
        self.nodes = set()
        for node in adj_list.keys():
            self.nodes.add(node)
            for connected_node in adj_list[node]:
                self.nodes.add(connected_node)

    def run(self,start_node):
        distances = {}
        distances[start_node] = 0
        self.marked = set()
        self.marked.add(start_node)
        queue = []
        queue.append(start_node)
        while len(queue)>0:
            v = queue[0]
            queue.pop(0)
            if v not in self.adj_list:
                continue
            i=0
            while(len(self.adj_list[v])>i):
                x = self.adj_list[v][i]
                i+=1
                if x in self.marked:
                    continue
                distances[x] = distances[v]+1
                self.marked.add(x)
                queue.append(x)
        return distances

