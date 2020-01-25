class Queue:

  def __init__(self):
    self.queue = []

  def isEmpty(self):
    return len(self.queue) == 0

  def enqueue(self, element):
    self.queue.append(element)

  def dequeue(self):
    if self.isEmpty():
      raise Exception("Cannot remove an element from an empty queue")
    else:
      dequeued_element = self.queue[0]
      self.queue = self.queue[1:]
      return dequeued_element


class BelmanNode:

  def __init__(self):
    self.parent = None
    self.shortest_path_estimate = 99999

  def __repr__(self):
    return "(Parent => " + str(self.parent) + ", d => " + str(self.shortest_path_estimate) + ")"
      

class BellmanFordWithFifo:

  def __init__(self, G, s):
    self.edges = G[0]
    self.vertices = G[1]
    self.start_vertex = s
    self.d = {vertex:BelmanNode() for vertex in self.vertices}
    self.active_vertices_queue = Queue()
  
  def initialise(self):
    self.d[self.start_vertex].shortest_path_estimate = 0
    self.active_vertices_queue.enqueue(self.start_vertex)

  def relax(self, edge):
    u, v, w = edge
    if self.d[v].shortest_path_estimate > self.d[u].shortest_path_estimate + w:
      self.d[v].shortest_path_estimate = self.d[u].shortest_path_estimate + w
      self.d[v].parent = u
      if v not in self.active_vertices_queue.queue:
        self.active_vertices_queue.enqueue(v)

  def compute(self):
    self.initialise()
    while not self.active_vertices_queue.isEmpty():
      u = self.active_vertices_queue.dequeue()
      for e in self.edges:
        if e[0] == u:
          self.relax(e)
    print(self.d)
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

print(BellmanFordWithFifo((e, v), 's').compute())
