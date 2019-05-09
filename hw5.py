# CSC 310 Homework 5
# Author: Charles Ryan Barrett
# Tower of Hanoi and tree traversal

# Problem 1 work area

# class Han:
#     def __init__(self, n):
#         self.a = []
#         self.b = []
#         self.c = []
#         o = 1
#         while o <= n:  # Need to initially populate stack A
#             self.a.append(o)
#             o += 1


def hanoi(n, frm, to, spare):
    if n == 1:
        print("Move disk", n, "from peg", frm, "to peg", spare)
        print()
        # if frm == 'A' and to == 'B':
        #     self.b.append(self.a.pop(0))
        # elif frm == 'B' and to == 'A':
        #     self.a.append(self.b.pop(0))
        # elif frm == 'A' and to == 'C':
        #     self.c.append(self.a.pop(0))
        # elif frm == 'C' and to == 'A':
        #     self.a.append(self.c.pop(0))
        # elif frm == 'B' and to == 'C':
        #     self.c.append(self.b.pop(0))
        # elif frm == 'C' and to == 'B':
        #     self.b.append(self.c.pop(0))
    elif n != 0:
        hanoi(n - 1, frm, spare, to)

        print("Move disk", n, "from peg", frm, "to peg", spare)
        print()
        # if frm == 'A' and spare == 'B':
        #     self.b.append(self.a.pop(0))
        # elif frm == 'B' and spare == 'A':
        #     self.a.append(self.b.pop(0))
        # elif frm == 'A' and spare == 'C':
        #     self.c.append(self.a.pop(0))
        # elif frm == 'C' and spare == 'A':
        #     self.a.append(self.c.pop(0))
        # elif frm == 'B' and spare == 'C':
        #     self.c.append(self.b.pop(0))
        # elif frm == 'C' and spare == 'B':
        #     self.b.append(self.c.pop(0))

        hanoi(n - 1, to, frm, spare)


#  Problem 2 work area
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class YourSolution(object):
    def __init__(self):
        self.L = []

    def inorderTraversal(self, root):
        # :type root: TreeNode
        # :rtype: List[int]
        if root.left:   # Base case is no more left or right nodes
            self.inorderTraversal(root.left)
        self.L.append(root.val)
        if root.right:
            self.inorderTraversal(root.right)

    def preorderTraversal(self, root):
        #   :type root: TreeNode
        #   :rtype: List[int]

        self.L.append(root.val)
        if root.left:   # Same base case as inorder
            self.preorderTraversal(root.left)
        if root.right:
            self.preorderTraversal(root.right)


def makeTree(L):
    if len(L) > 0:  # base case.
        if L[0]:
            t = TreeNode(L.pop(0))
            t.left = makeTree(L)
            t.right = makeTree(L)
            return t
        else:
            L.pop(0)    # removes the null value from the list
            return None


# Input area

go = True
tree = False
while go:
    print("1: Enter number of disks for Tower Of Hanoi and see steps")
    print("2: Create a Binary Tree")
    print("3: Show inorder and preorder traversal of binary Tree")
    print("0: Exit")
    inny = int(input("Input: "))
    if inny == 1:
        disk = int(input("Enter number of disks: "))
        while disk <= 0:
            print("Number of disks must be > 0")
            disk = int(input("Enter number of disks: "))
        hanoi(disk, 'A', 'B', 'C')
        print()
    if inny == 2:
        L = []  # empty list
        b = ""
        runforest = True
        while runforest:
            if len(L) > 0:   # initial value can't be Null
                b = input("Is this the end of that node? Y/N")
                print()
                if b.lower() == 'y':
                    L.append(None)
            if b.lower() != 'y':
                i = int(input("Enter values for the tree in (root, left, right): "))
                L.append(i)
            a = input("Are you done? Y/N")
            print("Values entered: ", L)
            if a.lower() == "y":
                print()
                runforest = False
        T = makeTree(L)     # this creates our tree
        tree = True
    if inny == 3:
        if tree:
            sol = YourSolution()
            sol.inorderTraversal(T)
            print("In order Traversal ", sol.L)
            sol.L = []    # Need to reset the list in the YourSolution class for the next traversal
            sol.preorderTraversal(T)
            print("Pre Order Traversal ", sol.L)
            print()
        else:
            print("There must be a tree made first!")
    if inny == 0:
        print("GoodBye!")
        go = False

#
# def Han(n,a,b,c):
#     if len(C) != n: # Base case, if c is n long, the movement is finished
#         print('Move disk ', a[len(a)-1], ' from peg A to peg B')    # printing out what happened.
#         b.append(a.pop())
#         if a:
#             print('Move disk ', a[len(a) - 1], ' from peg A to peg C')
#             c.append(a.pop())
#         elif c:
#             print('Move disk ', c[len(c) - 1], ' from peg C to peg B')
#             b.append(c.pop())
#             print('Move disk ', c[len(c) - 1], ' from peg C to peg A')
#             a.append(c.pop())
#             print('Move disk ', b[len(b) - 1], ' from peg B to peg A')
#             a.append(b.pop())
#
#         #   this is needed regardless of if and elif statements
#         print('Move disk ', b[len(b) - 1], ' from peg B to peg C')
#         c.append(b.pop())
#         Han(n, a, b, c)    # recursive call

