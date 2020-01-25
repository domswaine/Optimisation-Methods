class BelmanNode:
  def __init__(self):
    self.parent = None
    self.shortest_path_estimate = 99999
  def __repr__(self):
    return "(Parent => " + str(self.parent) + ", d => " + str(self.shortest_path_estimate) + ")"


class BellmanFord:

  def __init__(self, G, s):
    self.edges = G[0]
    self.vertices = G[1]
    self.start_vertex = s
    self.d = {vertex:BelmanNode() for vertex in self.vertices}

  def initialise(self):
    self.d[self.start_vertex].shortest_path_estimate = 0

  def relax(self, edge):
    u, v, w = edge
    new_weight = self.d[u].shortest_path_estimate + w
    if new_weight < self.d[v].shortest_path_estimate:
      self.d[v].shortest_path_estimate = new_weight
      self.d[v].parent = u

  def compute(self):
    self.initialise()
    
    for i in range(1, len(self.vertices)-1):
      for e in self.edges:
        self.relax(e)
    
    print(self.d)

    for e in self.edges:
      u, v, w = e
      if self.d[u].shortest_path_estimate > self.d[u].shortest_path_estimate + w:
        return False
    return True


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

print(BellmanFord((e, v), 's').compute())
