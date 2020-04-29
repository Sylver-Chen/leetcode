graph = {
    "a": ["b", "c"],
    "b": ["a", "c", "d"],
    "c": ["a", "b", "d", "e"],
    "d": ["b", "c", "e", "f"],
    "e": ["c", "d"],
    "f": ["d"],
}


def BFS(graph, s):
    queue = []
    queue.append(s)
    seen = set()
    seen.add(s)
    while len(queue) > 0:
        vertex = queue.pop(0)
        nodes = graph[vertex]
        for node in nodes:
            if node not in seen:
                queue.append(node)
                seen.add(node)
        print(vertex)


BFS(graph, "a")


def DFS(graph, s):
    stack = []
    stack.append(s)
    seen = set()
    seen.add(s)
    while len(stack) > 0:
        vertex = stack.pop()
        nodes = graph[vertex]
        for node in nodes:
            if node not in seen:
                stack.append(node)
                seen.add(node)
        print(vertex)


DFS(graph, "a")
