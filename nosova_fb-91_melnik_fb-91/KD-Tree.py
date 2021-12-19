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
        return '[' + str(self.data.x) + ', ' + str(self.data.y) + ']'
#складається з:
# - data have to be an Interval -- done
# - вказівника на лівого нащадка -- done
# - вказівника на правого нащадка --done
# - вказівника на предка -- done
# за замовчуванням усі вказівники вказують на нон, бо нода створюється окремо від дерева.
class KD_Tree:
    #function search:
        # contained by -- done
        # right of -- done
        # intersects
    #function add_node -- done
    #function show -- done
    #function contains -- done
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
# chained functions to show tree
    def print(self):
        buffer = []
        self.__print_recursive(self.root, buffer, "", "")
        print("\n".join(buffer))

    def __print_recursive(self, node, buffer, prefix, childrenPrefix):
        buffer.append(prefix + node.print_Node())

        if node.right_child != None:
            if node.left_child != None:
                self.__print_recursive(node.right_child, buffer, childrenPrefix + "├── ", childrenPrefix + "│   ")
            else:
                self.__print_recursive(node.right_child, buffer, childrenPrefix + "└── ", childrenPrefix + "    ")
        if node.left_child != None:
            self.__print_recursive(node.left_child, buffer, childrenPrefix + "└── ", childrenPrefix + "    ")

#---------------------------------------------------------------------------
#chained functions to find an interval in Tree
    def __go_find(self, currentNode, FindNode):
        if (currentNode.left_child != None or currentNode.right_child != None):  # if exists at least 1 child
            if(currentNode.data.x==FindNode.data.x and currentNode.data.y==FindNode.data.y):
                return True
            found=False
            if (currentNode.right_child != None and not found): found = self.__go_find(currentNode.right_child, FindNode)
            if (currentNode.left_child != None and not found): found = self.__go_find(currentNode.left_child, FindNode)
            return found
        else:  # no children
            if(currentNode.data.x==FindNode.data.x and currentNode.data.y==FindNode.data.y):
                return True
    def contains(self, user_data):
        FindNode = Node(user_data)
        found = self.__go_find(self.root, FindNode)
        if found:
            print('The KD-Tree contains this interval')
            return True
        else:
            print('The KD-Tree doesn`t contain this interval')
            return False

# ---------------------------------------------------------------------------
# search functions
    def __go_search_contained(self, currentNode, overNode, foundNodes, XY_f):
        XY=XY_f
        #check this node
        if(currentNode.data.x >= overNode.data.x and currentNode.data.y <= overNode.data.y):
            foundNodes.append(currentNode)
        #if exists at least one child - move on
        if(currentNode.right_child != None or currentNode.left_child != None):
            if XY:#if checking by x
                if(currentNode.data.x >= overNode.data.y and currentNode.left_child != None): # doesn`t intersect each other - no sense in going to right child - should go ONLY to the left child
                    self.__go_search_contained(currentNode.left_child, overNode, foundNodes, not XY)
                elif(currentNode.data.x <= overNode.data.x and currentNode.right_child != None): # no need to go to the left child if current is already lower than searched, because on the left there only lower and lower items
                    self.__go_search_contained(currentNode.right_child, overNode, foundNodes, not XY)
                else:
                    if(currentNode.right_child != None):self.__go_search_contained(currentNode.right_child, overNode, foundNodes, not XY)
                    if(currentNode.left_child != None):self.__go_search_contained(currentNode.left_child, overNode, foundNodes, not XY)
            else: # if checking by y
                if (currentNode.data.y <= overNode.data.x and currentNode.right_child != None):  # doesn`t intersect each other - no sense in going to left child - should go ONLY to the right child
                    self.__go_search_contained(currentNode.right_child, overNode, foundNodes, not XY)
                elif(currentNode.data.y >= overNode.data.y and currentNode.left_child != None): # no sense to go to the right child if current y is bigger that searched - go on the left
                    self.__go_search_contained(currentNode.left_child, overNode, foundNodes, not XY)
                else:
                    if(currentNode.right_child != None):self.__go_search_contained(currentNode.right_child, overNode, foundNodes, not XY)
                    if(currentNode.left_child != None):self.__go_search_contained(currentNode.left_child, overNode, foundNodes, not XY)
        return foundNodes

    def __go_search_intersects(self, currentNode, overNode, foundNodes, XY_f):
        XY=XY_f
        if(overNode.data.x<=currentNode.data.y and overNode.data.y>=currentNode.data.x):
            foundNodes.append(currentNode)
        if XY: # check by X
            if(currentNode.data.x > overNode.data.y): # doesnt intersect each other - no sense to go on the right
                if(currentNode.left_child != None): self.__go_search_intersects(currentNode.left_child, overNode, foundNodes, not XY)
            else:
                if (currentNode.left_child != None): self.__go_search_intersects(currentNode.left_child, overNode, foundNodes, not XY)
                if (currentNode.right_child != None): self.__go_search_intersects(currentNode.right_child, overNode, foundNodes, not XY)
        else:
            if(currentNode.data.y < overNode.data.x):
                if(currentNode.right_child != None): self.__go_search_intersects(currentNode.right_child, overNode, foundNodes, not XY)
            else:
                if (currentNode.left_child != None): self.__go_search_intersects(currentNode.left_child, overNode, foundNodes, not XY)
                if (currentNode.right_child != None): self.__go_search_intersects(currentNode.right_child, overNode,foundNodes, not XY)
        return foundNodes

    def search(self, user_data, whattodo):
        UserNode = Node(user_data)
        nodes=[]
        if (whattodo=="contained_by"):
            FoundNodes=self.__go_search_contained(self.root, UserNode, nodes, True)
        if(whattodo=="intersects"):
            FoundNodes=self.__go_search_intersects(self.root, UserNode, nodes, True)
        for i in range(0, len(FoundNodes)):
            print(FoundNodes[i].print_Node())

# ---------------------------------------------------------------------------
# right of functions

    def __go_search_right(self, currentNode, key, foundNodes, XY_f):
        XY=XY_f
        if(currentNode.data.x>=key):
            foundNodes.append(currentNode)
        if XY: # checked by X level
            if (currentNode.data.x >= key):
                    # if current x was on the right of key, have to check both children
                    if (currentNode.right_child != None): self.__go_search_right(currentNode.right_child, key, foundNodes, not XY)
                    if (currentNode.left_child != None): self.__go_search_right(currentNode.left_child, key, foundNodes, not XY)
             # если текущий узел не прошёл проверку - влево можно даже не идти, так как там находятся х которые только меньше текущего. Не работает для уровней, где сравнение происходило по у
            else:
                if(currentNode.right_child != None): self.__go_search_right(currentNode.right_child, key, foundNodes, not XY)
        else: #checked by Y level
            if (currentNode.data.y <= key): # go only to the right
                if(currentNode.right_child != None): self.__go_search_right(currentNode.right_child.key, foundNodes, not XY)
            else: #check both
                if (currentNode.right_child != None): self.__go_search_right(currentNode.right_child, key, foundNodes,not XY)
                if (currentNode.left_child != None): self.__go_search_right(currentNode.left_child, key, foundNodes,not XY)
        return foundNodes

    def right_of(self, user_data):
        nodes = []
        FoundNodes = self.__go_search_right(self.root, user_data, nodes, True)
        for i in range(0, len(FoundNodes)):
            print(FoundNodes[i].print_Node())

testtree=KD_Tree([2,3])
testnode=Node([2,5])
testnode1=Node([2,5])
testtree.add_node([4,6])
testtree.add_node([1,7])
testtree.add_node([3,8])
testtree.add_node([3,5])
testtree.add_node([0,8])
testtree.add_node([0,3])
testtree.print()
testtree.contains([3,8])
testtree.contains([9,9])
testtree.search([0,30], 'contained_by')
print("right of 1")
testtree.right_of(1)
print("intersects")
testtree.search([0,30], 'intersects')






