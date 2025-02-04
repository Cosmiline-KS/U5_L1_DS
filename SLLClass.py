# 2/4/25, Kennon Sauter, U5L1 ,SinglyLinkedList
class SinglyLinkedList:
  class SinglyNode:
    def __init__(self,value):
      self.value = value
      self.next = None
    def set_next(self,node):
      """Accepts node object and updates self.next"""
      if type(node) == type(self):
        self.next = node
      else:
        raise exception("Invaild node type")  
    # SinglyNode to-string
    def __str__(self):
      """Displays nodes"""
      return f"|{self.value}|"  
  ###################
  def __init__(self):
    self.head = None
    self.tail= None
    self.__size = 0


  def head_insert(self,value):
    """Accepts value and inserts new node at head"""
    node = self.SinglyNode(value)
    if self.__is_empty():
      self.head = node
      self.tail = node
    else:
      node.set_next(self.head)
      self.head = node
    self.__size += 1   

    
  def tail_insert(self,value):
    """Accepts value and inserts a new node at tail"""
    node = self.SinglyNode(value)
    if self.__is_empty():
      self.head = node
      self.tail = node
    else:  
      self.tail.set_next(node)
      self.tail = node
      
    self.__size += 1
    
  def head_remove(self):
    """removes and returns head value"""
    head = self.head
    self.head = head.next

    self.__size -= 1
    results = self.__is_empty()
    if results == True:
        self.head = None
        self.tail = None
    return head.value
  # SinglyLinkedList to-string
  def __len__(self):
    """Returns size"""
    return self.__size
  def __is_empty(self):
    """Checks to see if the linked list is empty"""
    if self.__size == 0:
      return True
    else:
      return False  
      
  def __str__(self):
    """Displays linked list"""
    out = "HEAD > "

    walk = self.head
    for i in range(self.__size):
        out += f"{walk} "
        walk = walk.next
        if walk != None:
            out += "-> "

    out += "< TAIL"
    return out
  
