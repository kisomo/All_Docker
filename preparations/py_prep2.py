
import numpy as np 

# ------------------------------------------------------------ BFS for shortest path ------------------------------------------------------------------------------------------
# give an undirected graph, use BFS to find the shortest path between two vertices.


#---------------------------------------------- print all paths from a node to a parent node ---------------------------------------------------------------------------------
#https://www.geeksforgeeks.org/find-paths-given-source-destination/
#Given acyclic graph find all the paths to a node from a parent node.
#Print all paths from a given source to a destination


#------------------------------------------------------- Bloomberg Interview 2 ---------------------------------------------------------------------------------------------------
#Given a m * n matrix mat of ones (representing soldiers) and zeros (representing civilians), return the indexes of the
#k weakest rows in the matrix ordered from the weakest to the strongest.
#A row i is weaker than row j, if the number of soldiers in row i is less than the number of soldiers in row j, or they
#have the same number of soldiers but i is less than j. Soldiers are always stand in the frontier of a row, that is,
#always ones may appear first and then zeros.


#------------------------------------------------------ check if a path exists in 2D matrix --------------------------------------------------------------------------------------
##https://www.geeksforgeeks.org/check-possible-path-2d-matrix/
#Given a 2D array(m x n). The task is to check if there is any path from top left to bottom right. In the matrix, -1 is considered as blockage (can’t go through this cell)
#and 0 is considered path cell (can go through it).

#method1

#method2

#-------------------------------------------------------------- BFS - for either printing paths or finding the shortest path ------------------------------------------------------
##https://www.educative.io/edpresso/how-to-implement-a-breadth-first-search-in-python

##https://www.geeksforgeeks.org/breadth-first-search-or-bfs-for-a-graph/




# -------------------------------------------------------- Rabin Karp algorithm -----------------------------------------------------------------------------------------------------

# ---------------------------------------------------------- KMP - Knuth Morris Pratt -----------------------------------------------------------------------------------------------


#--------------------------------------------------- BST ----------------------------------------------------------------------------------------------------------------------------
#https://www.geeksforgeeks.org/binary-search-tree-set-1-search-and-insertion/



#----------------------------------------------------------- bubble sort -----------------------------------------------------------------------------------------------------------
#https://www.geeksforgeeks.org/bubble-sort/



#-------------------------------------------------------- Newton Raphson ------------------------------------------------------------------------------------------------------------
#https://www.geeksforgeeks.org/program-for-newton-raphson-method/


#----------------------------------------------- Combinatorial sum ------------------------------------------------------------------------------------------------------------------
#https://www.geeksforgeeks.org/combinational-sum/?ref=leftbar-rightbar



#--------------------------------------------------------- count paths between 2 vertices --------------------------------------------------------------------------------------------
#https://www.geeksforgeeks.org/count-possible-paths-two-vertices/?ref=leftbar-rightbar



#------------------------------------------------------------------ string permutation ------------------------------------------------------------------------------------------------
#https://www.geeksforgeeks.org/print-all-permutations-of-a-string-in-java/?ref=leftbar-rightbar





#------------------------------------------------------ subset sums ------------------------------------------------------------------------------------------------------------------
#https://www.geeksforgeeks.org/subset-sum-backtracking-4/?ref=leftbar-rightbar



#--------------------------------------------------- print possible paths from top left to bottom righ --------------------------------------------------------------------------------
#https://www.geeksforgeeks.org/print-all-possible-paths-from-top-left-to-bottom-right-of-a-mxn-matrix/


#no diagonal movements

# allow diagonal movements

# allow blockage/restrictions


#------------------------------------------ count number of paths from top-left to bottom right ------------------------------------------------------------------------------------
#https://www.geeksforgeeks.org/count-possible-paths-top-left-bottom-right-nxm-matrix/


#no diagonal movements

# allow diagonal movements

# allow blockage/restrictions

#method 1

#method 2




#--------------------------------------------------------- delete recurring characters in a string ---------------------------------------------------------------------------
# 13). Given a string as your input, delete any reoccuring character, and return the new string.




#--------------------------------------- split string using newline ---------------------------------------------------------------------------------------------------------
# 12). write a python program to split strings using newline delimiter.




#------------------------------------------- extract digits from string ----------------------------------------------------------------------------------------------------
# 11). write a program to extract digits from a given string




#--------------------------------------- join strings ---------------------------------------------------------------------------------------------------------------------
# 10). write a program to join two strings 



#------------------------------------------------- Binary search ---------------------------------------------------------------------------------------------------------
# 9). write a program to implement binary search.



#----------------------------------------- search an element in an array --------------------------------------------------------------------------------------------------
# 8). Given an array arr[] of n elements, write a function to search a given element x in arr[]




#------------------------------------------- number of words in a sentence -----------------------------------------------------------------------------------------------
# 7). write a program print the number of words in a given sentence.



#-------------------------------------------- print duplicates -----------------------------------------------------------------------------------------------------------
# 6). write a program to print set of duplicates in a list.



#------------------------------------------- palindrome -----------------------------------------------------------------------------------------------------------------
#5). write a Python program to check whether a string is a palindrome or not (Madam)



#----------------------------------- reverse list -----------------------------------------------------------------------------------------------------------------------
#4). print a list in reverse



#------------------------------------ fibonacci --------------------------------------------------------------------------------------------------------------------------
#3). write a Python program to print Fibinacci Series



#---------------------------- sort elements in a list --------------------------------------------------------------------------------------------------------------------
#2). write a sort function to sort the elements in a list



#------------------------------------------------- print prime numbers ----------------------------------------------------------------------------------------------------
#1). write a python program to print prime numbers between 100 and 200.



#----------------------------- largest range in an array ---------------------------------------------------------------------------------------------------------------------
#https://www.youtube.com/watch?v=TgCKJU3JvO4

#Write a function that takes in an array of integers and returns an array of length 2 representing the largest range of numbers contained in that array. The first number in the output
#array should be the first number in the range while the second number should be the last number in the range. A range of numbers is defined as a set of numbers that come right after each 
#other in the set of real integers. For instance, the output array [2,6] represents the range [2,3,4,5,6] which is a range of length 5. Note that numbers do not need to be ordered or adjacent in the array in order 
#to form a range. Assume that there will only be one largest range. 
#sample input: [1,11,3,0,15,5,2,4,10,7,12,6]
#sample output: [0,7]


###############################################################################################################################################################################
###################################### CODE ONE ###################################################################################################################################
###############################################################################################################################################################################

# ------------------------------------------------------------ BFS for shortest path ------------------------------------------------------------------------------------------
# give an undirected graph, use BFS to find the shortest path between two vertices.

class graph():
    def __init__(self,V):
        self.V = V 
        self.adj = [[] for i in range(V)]
    def add_node(self,u,v):
        self.adj[u].append(v)
    def return_node(self,u):
        return self.adj[u]
    def adjacent_nodes(self,u):
        #res = [i for i in self.adj[u]]
        #return res
        pass

r = graph(4)
r.add_node(0,1)
r.add_node(0,2)
r.add_node(0,3)
r.add_node(1,3)
r.add_node(2,0)
r.add_node(2,1)

#print(r)

def shortest_path(graph, start, goal):
    explored = [] 
    # Queue for traversing the graph in the BFS
    queue = [[start]]
      
    # If the desired node is  reached
    if start == goal:
        print("Same Node")
        return
    # Loop to traverse the graph with the help of the queue
    while queue:
        path = queue.pop(0)
        node = path[-1] 
        # Codition to check if the current node is not visited
        if node not in explored:
            neighbours = graph.return_node(node) #graph[node]
            # Loop to iterate over the neighbours of the node
            for neighbour in neighbours:
                new_path = list(path)
                new_path.append(neighbour)
                queue.append(new_path)
                # Condition to check if the neighbour node is the goal
                if neighbour == goal:
                    print("Shortest path = ", *new_path)
                    return
            explored.append(node)
    # Condition when the nodes are not connected
    print("So sorry, but a connecting path doesn't exist :(")
    return

print(shortest_path(r,2,3))



#---------------------------------------------- print all paths from a node to a parent node ---------------------------------------------------------------------------------
#https://www.geeksforgeeks.org/find-paths-given-source-destination/
#Given acyclic graph find all the paths to a node from a parent node.
#Print all paths from a given source to a destination

'''
class graph2():
    def __init__(self,V):
        self.V = V 
        self.adj = [[] for i in range(V)]

    def return_node(self,u):
        return self.adj[u] 

    def add_node(self, u,v):
        self.adj[u].append(v)

    def printAllPathsUntil(self,s,d,path,visited):
        visited[s] = True
        path.append(s)
        if(s == d):
            print(path)
            return
        else:
            for k in self.adj[s]:
                visited[k] = True
                self.printAllPathsUntil(k,d,path,visited)
        path.pop()
        visited[s] = False

    def printPaths(self,s,d):
        visited =[False]*(self.V)
        path = []
        self.printAllPathsUntil(s,d,path,visited)

r = graph2(4)
r.add_node(0,1)
r.add_node(0,2)
r.add_node(0,3)
r.add_node(1,3)
r.add_node(2,0)
r.add_node(2,1)


r.printPaths(0,3)
'''

#------------------------------------------------------- Bloomberg Interview 2 ---------------------------------------------------------------------------------------------------
#Given a m * n matrix mat of ones (representing soldiers) and zeros (representing civilians), return the indexes of the
#k weakest rows in the matrix ordered from the weakest to the strongest.
#A row i is weaker than row j, if the number of soldiers in row i is less than the number of soldiers in row j, or they
#have the same number of soldiers but i is less than j. Soldiers are always stand in the frontier of a row, that is,
#always ones may appear first and then zeros.

class Solution:
    def kWeakestRows(self, mat, k):
        res =[]
        for i in range(len(mat)):
            res.append((i,sum(mat[i])))
        res.sort(key=lambda x : x[1])
        res2 = [i[0] for i in res]
        print(res2[:k])
        return res2[:k]
        
            
print("------- soln --------------")
if __name__ == "__main__":

    soln = Solution()
    mat = [[1, 1, 0, 0, 0],
           [1, 1, 1, 1, 0],
           [1, 0, 0, 0, 0],
           [1, 1, 0, 0, 0],
           [1, 1, 1, 1, 1]]
    k = 3
    assert soln.kWeakestRows(mat, k) == [2, 0, 3]

    mat = [[1, 0, 0, 0],
           [1, 1, 1, 1],
           [1, 0, 0, 0],
           [1, 0, 0, 0]]
    k = 2
    assert soln.kWeakestRows(mat, k) == [0, 2]



#------------------------------------------------------ check if a path exists in 2D matrix --------------------------------------------------------------------------------------
##https://www.geeksforgeeks.org/check-possible-path-2d-matrix/
#Given a 2D array(m x n). The task is to check if there is any path from top left to bottom right. In the matrix, -1 is considered as blockage (can’t go through this cell)
#and 0 is considered path cell (can go through it).

#method1

def isPath(mat):
    m,n = len(mat),len(mat[0])
    #mat[0][0] = 1
    q = []
    #directions = [down,right]
    directions = [[0,-1],[1,0]]
    q.append((0,0))
    while(len(q) > 0):
        p = q[0]
        q.pop(0)
        if( p == (m-1,n-1)):
            #print("Yes")
            return True 
        for k in range(len(directions)):
            a = p[0] + directions[k][0]
            b = p[1] + directions[0][k]
            if(a >=0 and b >=0 and a <m and b < n and mat[a][b] != -1):
                q.append((a,b))
        #print("No")
        return False 


# Given array
arr = [ [ 0,  0,  0, -1,  0 ],
        [ -1, 0,  0, -1, -1 ],
        [ 0,  0,  0,  0,  0 ],
        [ -1, 0, -1,  0,  0 ],
        [ 0,  0, -1,  0,  0 ] ]
 
print(isPath(arr))

#method2

def isPath2(mat):
    m,n = len(mat),len(mat[0])
    mat[0][0] = 1
    for i in range(1,m):
        if(mat[i][0] != -1):
            mat[i][0] = mat[i-1][0]
    for j in range(1,n):
        if(mat[0][j] != -1):
            mat[0][j] = mat[0][j-1]
    for i in range(1,m):
        for j in range(1,n):
            if(mat[i][j] != -1):
                mat[i][j] = max(mat[i-1][j],mat[i][j-1])
    return (mat[m-1][n-1] == 1)

print(isPath2(arr))

#-------------------------------------------------------------- BFS - for either printing paths or finding the shortest path ------------------------------------------------------
##https://www.educative.io/edpresso/how-to-implement-a-breadth-first-search-in-python

print("\n")

class graph():
    def __init__(self,V):
        self.V = V 
        self.adj = [[] for i in range(V)]
    def add_node(self,u,v):
        self.adj[u].append(v)
    def return_node(self,u):
        return self.adj[u]
    # Function to print a BFS of graph
    def BFS(self, s):
        # Mark all the vertices as not visited
        visited = [False] * (self.V) #(max(self.adj) + 1)
        # Create a queue for BFS
        queue = []
        # Mark the source node as visited and enqueue it
        queue.append(s)
        visited[s] = True
 
        while queue:
            # Dequeue a vertex from queue and print it
            s = queue.pop(0)
            print (s, end = " ")
            # Get all adjacent vertices of the dequeued vertex s. If a adjacent
            # has not been visited, then mark it visited and enqueue it
            for i in self.return_node(s):
                if visited[i] == False:
                    queue.append(i)
                    visited[i] = True
 

#A =0, B = 1, C = 2, D = 3, E = 4, F = 5 

r = graph(6)
r.add_node(0,1)
r.add_node(0,2)
r.add_node(1,3)
r.add_node(1,4)
r.add_node(2,5)
r.add_node(4,5)


visited = [] # List to keep track of visited nodes.
queue = []     #Initialize a queue

def bfs(visited, graph, node):
  visited.append(node)
  queue.append(node)

  while queue:
    s = queue.pop(0) 
    print (s, end = " ") 

    for neighbour in graph.return_node(s):
      if neighbour not in visited:
        visited.append(neighbour)
        queue.append(neighbour)

# Driver Code
bfs(visited, r, 1)


##https://www.geeksforgeeks.org/breadth-first-search-or-bfs-for-a-graph/

print("\n")

g = graph(4)
g.add_node(2,0)
g.add_node(2,3)
g.add_node(0,1)
g.add_node(0,2)
g.add_node(1,2)
g.add_node(3,3)

g.BFS(2)



# -------------------------------------------------------- Rabin Karp algorithm -----------------------------------------------------------------------------------------------------

# ---------------------------------------------------------- KMP - Knuth Morris Pratt -----------------------------------------------------------------------------------------------


#--------------------------------------------------- BST ----------------------------------------------------------------------------------------------------------------------------
#https://www.geeksforgeeks.org/binary-search-tree-set-1-search-and-insertion/




#----------------------------------------------------------- bubble sort -----------------------------------------------------------------------------------------------------------
#https://www.geeksforgeeks.org/bubble-sort/



#-------------------------------------------------------- Newton Raphson ------------------------------------------------------------------------------------------------------------
#https://www.geeksforgeeks.org/program-for-newton-raphson-method/


#----------------------------------------------- Combinatorial sum ------------------------------------------------------------------------------------------------------------------
#https://www.geeksforgeeks.org/combinational-sum/?ref=leftbar-rightbar



#--------------------------------------------------------- count paths between 2 vertices --------------------------------------------------------------------------------------------
#https://www.geeksforgeeks.org/count-possible-paths-two-vertices/?ref=leftbar-rightbar



#------------------------------------------------------------------ string permutation ------------------------------------------------------------------------------------------------
#https://www.geeksforgeeks.org/print-all-permutations-of-a-string-in-java/?ref=leftbar-rightbar





#------------------------------------------------------ subset sums ------------------------------------------------------------------------------------------------------------------
#https://www.geeksforgeeks.org/subset-sum-backtracking-4/?ref=leftbar-rightbar



#--------------------------------------------------- print possible paths from top left to bottom righ --------------------------------------------------------------------------------
#https://www.geeksforgeeks.org/print-all-possible-paths-from-top-left-to-bottom-right-of-a-mxn-matrix/


#no diagonal movements

# allow diagonal movements

# allow blockage/restrictions


#------------------------------------------ count number of paths from top-left to bottom right ------------------------------------------------------------------------------------
#https://www.geeksforgeeks.org/count-possible-paths-top-left-bottom-right-nxm-matrix/


#no diagonal movements

# allow diagonal movements

# allow blockage/restrictions

#method 1

#method 2




#--------------------------------------------------------- delete recurring characters in a string ---------------------------------------------------------------------------
# 13). Given a string as your input, delete any reoccuring character, and return the new string.




#--------------------------------------- split string using newline ---------------------------------------------------------------------------------------------------------
# 12). write a python program to split strings using newline delimiter.




#------------------------------------------- extract digits from string ----------------------------------------------------------------------------------------------------
# 11). write a program to extract digits from a given string




#--------------------------------------- join strings ---------------------------------------------------------------------------------------------------------------------
# 10). write a program to join two strings 



#------------------------------------------------- Binary search ---------------------------------------------------------------------------------------------------------
# 9). write a program to implement binary search.



#----------------------------------------- search an element in an array --------------------------------------------------------------------------------------------------
# 8). Given an array arr[] of n elements, write a function to search a given element x in arr[]




#------------------------------------------- number of words in a sentence -----------------------------------------------------------------------------------------------
# 7). write a program print the number of words in a given sentence.



#-------------------------------------------- print duplicates -----------------------------------------------------------------------------------------------------------
# 6). write a program to print set of duplicates in a list.



#------------------------------------------- palindrome -----------------------------------------------------------------------------------------------------------------
#5). write a Python program to check whether a string is a palindrome or not (Madam)



#----------------------------------- reverse list -----------------------------------------------------------------------------------------------------------------------
#4). print a list in reverse



#------------------------------------ fibonacci --------------------------------------------------------------------------------------------------------------------------
#3). write a Python program to print Fibinacci Series



#---------------------------- sort elements in a list --------------------------------------------------------------------------------------------------------------------
#2). write a sort function to sort the elements in a list



#------------------------------------------------- print prime numbers ----------------------------------------------------------------------------------------------------
#1). write a python program to print prime numbers between 100 and 200.



#----------------------------- largest range in an array ---------------------------------------------------------------------------------------------------------------------
#https://www.youtube.com/watch?v=TgCKJU3JvO4

#Write a function that takes in an array of integers and returns an array of length 2 representing the largest range of numbers contained in that array. The first number in the output
#array should be the first number in the range while the second number should be the last number in the range. A range of numbers is defined as a set of numbers that come right after each 
#other in the set of real integers. For instance, the output array [2,6] represents the range [2,3,4,5,6] which is a range of length 5. Note that numbers do not need to be ordered or adjacent in the array in order 
#to form a range. Assume that there will only be one largest range. 
#sample input: [1,11,3,0,15,5,2,4,10,7,12,6]
#sample output: [0,7]



























