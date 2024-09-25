def dfs_recursive_(start_node,adj_list:dict,marked:set,time = 1):
    """
    helper function
    Will run dfs on start_node,
    return the dfs tree of start_node (and only that)
    """
    if start_node in marked:
        return []
    marked.add(start_node)
    result = []
    for node in adj_list[start_node]:
        result+=dfs_recursive_(node,adj_list,marked,time+1)
    pass
def dfs_recursive_main(adj_list:dict,start_node = None):

    marked = []
    dfs_tress = []
    nodes = list(adj_list.keys())
    if start_node is not None:
        nodes = [start_node] + nodes.remove(start_node)
    for node in nodes:
        dfs_tress+=dfs_recursive_(node,adj_list)
    return dfs_tress


class DFS:
    """
    DFS implmentation on adjacency list of a directed graph
    """
    def __init__(self,adj_list) -> None:
        self.adj_list = adj_list
        self.nodes = set()
        for node in adj_list.keys():
            self.nodes.add(node)
            for connected_node in adj_list[node]:
                self.nodes.add(connected_node)
    def run(self,start_node = None,dfs_type = 'iterative'):

        dfs_tress = []
        self.time = 1
        self.marked = set()
        if dfs_type == 'recursive':
            dfs_func = self.recursive_dfs
        else:
            dfs_func = self.iterative_dfs
        if start_node is not None:
            dfs_tress.append(dfs_func(start_node))
        for node in self.nodes:
            result = dfs_func(node)
            if len(result)>0:
                dfs_tress.append(result)
        return dfs_tress
    def recursive_dfs(self,start_node):
        if start_node in self.marked:
            return []
        start_time = self.time
        self.marked.add(start_node)
        self.time = self.time +1
        result = []
        for node in self.adj_list[start_node]:
            result+=self.recursive_dfs(node)
        result+=[(start_node,start_time,self.time)]
        self.time+=1
        return result
    def iterative_dfs(self,start_node):
        result = []
        stack = []
        self.marked.add(start_node)
        d = {}
        f = {}
        d[start_node] = self.time
        self.time+=1
        stack.append(start_node)
        while len(stack)>0:
            u = stack[0]
            i = 0
            while((u not in self.marked) and len(self.adj_list[u])<i):
                v = self.adj_list[u][i]
                d[v] = self.time
                self.time+=1
                stack.append(v)
                u = v
            stack.pop()
            f[u] = self.time
            result.append((u,d[u],f[u]))
            self.time+=1
        return result


    # """
    # DFS implmentation on adjacency list of a directed graph
    # input:
    # adjacency list - a dict of lists, each key should represent a node.
    # The value should be a list of nodes that are connected to the key node.
    # start_node - key of the starting node in the adjacency list, if none will chose the first key of the dict.

    # example:
    # {
    #     'A' : ['B','C'],
    #     'B' : ['C'],
    #     'C' : ['D']
    # }
    # Represents a graph in which
    # The edges are A->B,A->C,B->C,C->D

    # The start node should be a key representation of a node.

    # The output will be a list of lists, each list will represent a dfs-tree
    # Each element of the list will be a node with openining and closing time intervals, i.e : [('A',1,10),....]