inf = 99999

class PriorityQueueNode:

  def __init__(self, element, priority):
    self.element = element
    self.priority = priority


class PriorityQueue:

  def __init__(self):
    self.queue = []

  def isEmpty(self):
    return len(self.queue) == 0

  def insert(self, node):
    i = 0
    while i < len(self.queue) and self.queue[i].priority <= node.priority:
      i +=1
    self.queue.insert(i, node)

  def remove(self):
    if self.isEmpty():
      raise Exception("Cannot remove an element from an empty queue")
    else:
      node = self.queue[0]
      self.queue = self.queue[1:]
      return node


class TreeNode:

  def __init__(self):
    self.parent = None
    self.shortest_path_estimate = inf

  def __repr__(self):
    return "(Parent => " + str(self.parent) + ", d => " + str(self.shortest_path_estimate) + ")"


class Dijkstra:
  
  def __init__(self, g, s):
    self.edges = g[0]
    self.vertices = g[1]
    self.start_vertex = s
    self.s = set()
    self.q = PriorityQueue()
    self.d = {vertex:TreeNode() for vertex in self.vertices}

  def insert(self, element, priority, parent):
    self.d[element].shortest_path_estimate = priority
    self.d[element].parent = parent
    self.q.insert(PriorityQueueNode(element, priority))

  def initialise(self):
    for vertex in self.vertices:
      if vertex == self.start_vertex:
        self.insert(vertex, 0, None)
      else:
        self.insert(vertex, inf, None)

  def relax(self, edge):
    u, v, w = edge
    new_path_estimate = self.d[u].shortest_path_estimate + w
    if self.d[v].shortest_path_estimate > new_path_estimate:
      self.insert(v, new_path_estimate, u)

  def compute(self):
    self.initialise()
    
    while not self.q.isEmpty():
      node = self.q.remove()
      u = node.element
      priority = node.priority
      
      if u not in self.s:
        self.s.add(u)

        for edge in self.edges:
          if edge[0] == u:
            self.relax(edge)
        
        print(self.d)


e = [
     ('s', 'u', 10),
     ('s', 'x', 5),
     ('u', 'x', 2),
     ('x', 'u', 3),
     ('u', 'v', 1),
     ('x', 'v', 9),
     ('x', 'y', 2),
     ('y', 's', 7),
     ('v', 'y', 4),
     ('y', 'v', 6)
]
v = ['s', 'u', 'v', 'x', 'y']

Dijkstra((e, v), 's').compute()
