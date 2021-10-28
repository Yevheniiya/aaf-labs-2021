class Interval:
    def _check(self, v1, v2):
        if isinstance(v1, int) and isinstance(v2, int):
            return True
        else:
            print('X and Y must be an integer!')
            return False
    def __init__(self, user_x, user_y):
        if self._check(user_x, user_y):
            self.x=user_x
            self.y=user_y
            print ('Interval successfully created!')
        else: print('The Interval was not created!')
class Node:
    def _check(self, dt):
        if isinstance(dt, Interval):return True
        if isinstance(dt, list):
            if(len(dt)==2 and isinstance(dt[0], int) and isinstance(dt[1], int)):
                convert_d=Interval(dt[0], dt[1])
                return convert_d
            else:
                print('Incorrect number of elements in array or non-integer value is passed')
                return False
        else:
            print('Wrong datatype is transferred')
            return False
    def __init__(self, user_data, p=None, lch=None, rch=None):
        decision = self._check(user_data)
        if isinstance(decision, bool):
            if decision:
                self.data=user_data
                self.left_child = lch
                self.right_child = rch
                self.parent = p
                print('New Node is created!')
            else: print('The Node was not created')
        elif isinstance(decision, Interval):
            self.data=decision
            self.left_child = lch
            self.right_child = rch
            self.parent = p
            print('New Node is created!')
        else: print('The Node was not created')
    def print_Node(self):
        print('[',self.data.x,',',self.data.y,']')
#складається з:
# - data have to be an Interval -- done
# - вказівника на лівого нащадка -- done
# - вказівника на правого нащадка --done
# - вказівника на предка -- done
# за замовчуванням усі вказівники вказують на нон, бо нода створюється окремо від дерева.
class KD_Tree:
    # function add_node -- done
    #function show -- done, but shows tree not in pretty way
    #function contains ---- but shows a message only if found (have to implement some return mechanism in the case if the tree doesnt contain provided interval)
    #consists of root + leafs - root is stored within datastructure
    def _check(self, user_data): #function to check what data type we`re transferring.
        if isinstance(user_data, Node):
            return True
        elif (isinstance(user_data, list) and len(user_data)==2 and isinstance(user_data[0], int) and isinstance(user_data[1], int)) or isinstance(user_data, Interval): #try to convert list to Node;
            convert_Nd=Node(user_data)
            return convert_Nd
        else:
            print('Wrong datatype is transferred. Entered data must be either an Interval object, Node object or an array of two integer!')
            return False
    def __init__(self, user_root): #при создании дерева - у него должен быть только корень представляющий собой ту же ноду.
                                # По этому, при создании дерева создаётся и первая нода. Соответственно, ей нужно передать данные (интервал)
                                # Дерево может быть создано c переданным интервалом, координатами или нодой.
        decision = self._check(user_root)
        if isinstance(decision, bool): # transferred Node or failed
            if decision:
                self.root=user_root
                print('New KD-Tree is created!')
            else: print('KD-Tree was not created')
        elif isinstance(decision, Node):
            self.root=decision
            print('New KD-Tree is created!')
        else: print('KD-Tree was not created')
#---------------------------------------------------------------------------
# chained functions to add nodes
    def __go_func(self, NewNode, currentNode, XY_f):
        XY=XY_f
        if (currentNode.left_child != None and currentNode.right_child != None): #if both childs exists - we cant insert and can only move.
            #decide where to move
            if XY:  # comparing by x
                if (currentNode.data.x > NewNode.data.x or currentNode.data.x == NewNode.data.x):  # current x is bigger than added x -> move to left
                    self.__go_func(NewNode, currentNode.left_child, not XY)
                else:
                    self.__go_func(NewNode, currentNode.right_child, not XY)
            else:  # comparing by y
                if (currentNode.data.y > NewNode.data.y or currentNode.data.y == NewNode.data.y):
                    self.__go_func(NewNode, currentNode.left_child, not XY)
                else:
                    self.__go_func(NewNode, currentNode.right_child, not XY)
        elif (currentNode.left_child != None):#only left child exists
            if XY:  # comparing by x
                if (currentNode.data.x > NewNode.data.x or currentNode.data.x == NewNode.data.x):  # current x is bigger than added x -> move to left
                    self.__go_func(NewNode, currentNode.left_child, not XY)
                else:
                    currentNode.right_child = NewNode
                    NewNode.parent = currentNode
            else: # comparing by y
                if (currentNode.data.y > NewNode.data.y or currentNode.data.y == NewNode.data.y):
                    self.__go_func(NewNode, currentNode.left_child, not XY)
                else:
                    currentNode.right_child = NewNode
                    NewNode.parent = currentNode
        elif (currentNode.right_child != None): #only right child exists
            if XY:  # comparing by x
                if (currentNode.data.x > NewNode.data.x or currentNode.data.x == NewNode.data.x):  # current x is bigger than added x -> move to left
                    currentNode.left_child = NewNode
                    NewNode.parent = currentNode
                else:
                    self.__go_func(NewNode, currentNode.right_child, not XY)
            else: # comparing by y
                if (currentNode.data.y > NewNode.data.y or currentNode.data.y == NewNode.data.y):
                    currentNode.left_child = NewNode
                    NewNode.parent = currentNode
                else:
                    self.__go_func(NewNode, currentNode.right_child, not XY)
        else:  # no children at all
            if XY:  # comparing by x
                if (currentNode.data.x > NewNode.data.x or currentNode.data.x == NewNode.data.x):  # current x is bigger than added x -> NewNodde is a leftchild
                    currentNode.left_child = NewNode
                    NewNode.parent = currentNode
                else:
                    currentNode.right_child = NewNode
                    NewNode.parent = currentNode
            else:  # comparing by y
                if (currentNode.data.y > NewNode.data.y or currentNode.data.y == NewNode.data.y):
                    currentNode.left_child = NewNode
                    NewNode.parent = currentNode
                else:
                    currentNode.right_child = NewNode
                    NewNode.parent = currentNode
    def add_node(self, user_data):#here we should check where to add data by algorithm
        NewNode=Node(user_data) # create new node
        self.__go_func(NewNode, self.root, True)
#---------------------------------------------------------------------------
# chained functions to show tree  --------- not in pretty way
    def __go_show(self, currentNode, indent):
        if(currentNode.left_child != None or currentNode.right_child != None): # if exists at least 1 child
            currentNode.print_Node()
            if(currentNode.right_child != None):self.__go_show(currentNode.right_child, 0)
            if (currentNode.left_child != None): self.__go_show(currentNode.left_child, 0)
        else: # no children
            currentNode.print_Node()
    def show(self):
        self.__go_show(self.root, 0)
#---------------------------------------------------------------------------
#chained functions to find an interval ---- but shows a message only if found (have to implement some return mechanism in the case if the tree doesnt contain provided interval)
    def __go_find(self, currentNode, FindNode):
        if (currentNode.left_child != None or currentNode.right_child != None):  # if exists at least 1 child
            if(currentNode.data.x==FindNode.data.x and currentNode.data.y==FindNode.data.y):
                print('The KD-Tree contains this interval')
            if (currentNode.right_child != None): self.__go_find(currentNode.right_child, FindNode)
            if (currentNode.left_child != None): self.__go_find(currentNode.left_child, FindNode)
        else:  # no children
            if(currentNode.data.x==FindNode.data.x and currentNode.data.y==FindNode.data.y):
                print('The KD-Tree contains this interval')
    def contains(self, user_data):
        FindNode = Node(user_data)
        self.__go_find(self.root, FindNode)

testtree=KD_Tree([2,3])
testnode=Node([2,5])
testnode1=Node([2,5])
testtree.add_node([4,6])
testtree.add_node([1,7])
testtree.add_node([3,8])
testtree.add_node([3,5])
testtree.add_node([0,8])
testtree.add_node([0,3])
testtree.show()
testtree.contains([2,3])
testtree.contains([4,6])
testtree.contains([3,8])






