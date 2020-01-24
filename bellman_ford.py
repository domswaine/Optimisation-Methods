class BelmanNode:
  def __init__(self):
    self.parent = None
    self.shortest_path_estimate = 99999
  def __repr__(self):
    return "(Parent => " + str(self.parent) + ", d => " + str(self.shortest_path_estimate) + ")"

def initialisation(s, vertices):
  d = {vertex:BelmanNode() for vertex in vertices}
  d[s].shortest_path_estimate = 0
  return d

def relax(edge, d):
  u, v, w = edge
  new_weight = d[u].shortest_path_estimate + w
  if new_weight < d[v].shortest_path_estimate:
    d[v].shortest_path_estimate = new_weight
  return d

def bellman_ford(G, s):
  edges, vertices = G
  d = initialisation(s, vertices)
  
  for i in range(1, len(vertices)-1):
    for e in edges:
      d = relax(e, d)
  print(d)

  for e in edges:
    u, v, w = e
    if d[u].shortest_path_estimate > d[u].shortest_path_estimate + w:
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

print(bellman_ford((edges, vertices), 's'))
