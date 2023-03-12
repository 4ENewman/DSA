
# A node is a basic unit of a data structure, such as a linked list or tree data structure. Nodes contain data and also may link to other nodes. Links between nodes are often implemented by pointers.

class Node:
  def __init__(self, value, link_node=None):
    self.value = value
    self.link_node = link_node
    
  def set_link_node(self, link_node):
    self.link_node = link_node
    
  def get_link_node(self):
    return self.link_node
  
  def get_value(self):
    return self.value

yacko = Node('likes to yak')
wacko = Node("has a penchant for hoarding snacks")
dot = Node("enjoys spending time in movie lots")

yacko.set_link_node(dot)
dot.set_link_node(wacko)

dots_data = yacko.get_link_node().get_value()
# dots_data = yacko's node links to dot's node -> get link node's value aka dot
# yacko class ('likes to yak', dot)
print(yacko.get_link_node())
print(dots_data)
wackos_data = dot.get_link_node().get_value()
print(wackos_data)