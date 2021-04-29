
#sudo docker build . -t interview_prep:1.0.0

#sudo docker images

#sudo docker run -d -p 5000:5000 interview_prep:1.0.0
#sudo docker run --rm -it interview_prep:1.0.0

'''
FROM ubuntu:latest
RUN apt-get update -y
RUN apt-get install -y python3-pip python3-dev build-essential


FROM python:3.8
RUN pip install virtualenv 
ENV VIRTUAL_ENV=/venv 
RUN virtualenv venv -p python3 
ENV PATH="$VIRTUAL_ENV/bin:$PATH"


COPY . /app
WORKDIR /app
RUN pip3 install -r requirements.txt


ENTRYPOINT ["python3"]
CMD ["py_prep.py"]




'''

import numpy as np 

###################################################### HARD #################################################################################################

#https://www.youtube.com/watch?v=TgCKJU3JvO4


'''
Write a function that takes in an array of integers and returns an array of length 2 representing the largest range of numbers contained in that array. The first number in the output
array should be the first number in the range while the second number should be the last number in the range. A range of numbers is defined as a set of numbers that come right after each 
other in the set of real integers. For instance, the output array [2,6] represents the range [2,3,4,5,6] which is a range of length 5. Note that numbers do not need to be ordered or adjacent in the array in order 
to form a range. Assume that there will only be one largest range. 

sample input: [1,11,3,0,15,5,2,4,10,7,12,6]
sample output: [0,7]

'''

# [0,1,2,3,4,5,6,7,10,11,15] sorting runs in o(nlog(n)) but we something that runs in linear time - .

#save the numbers in a hash table - this runs in o(1)

#use 0 as the key for each element
#it runs in linear time because we look at each number once.

'''

def largestRange(array):
    #create the hash table
    numbers = {x:0 for x in array}
    left = right = 0

    for number in array:
        #if numbers[number] ==0:
            left_count = number -1
            right_count = number +1

            while left_count in numbers:
                numbers[left_count] = 1  # O(1)
                left_count -=1
            left_count +=1

            while right_count in numbers:
                numbers[right_count] =1
                right_count +=1
            right_count -=1

            if (right - left) <= (right_count - left_count):
                right = right_count
                left = left_count

    return [left, right]

arr = [1,11,3,0,15,5,2,4,10,7,12,6]
print(largestRange(arr))

'''
            



##################################################### EASY ##################################################################################################

#https://www.youtube.com/watch?v=RNRmh9hMmtA

'''
The Fibonacci sequence is defined as follows: the first number of the sequence is 0 and the second number is 1. The nth number is the sum of the (n-1)th and (n-2)th numbers.
Write a function that takes in an integer n and returns the nth Fibonacci number.

sample input: 6
sample output: 5  {0,1,1,2,3,5}

'''


'''
def getnthfib(n):
    # write code here
    if n ==1:
        return 0
    elif n <=3:
        return 1
    else:
        return getnthfib(n-1) + getnthfib(n-2)

print(getnthfib(6))    

def getnthfib2(n, calculated = {1:0, 2:1, 3:1}):
    # write code here
    if n in calculated:
        return calculated[n]
    else:
        calculated[n] = getnthfib2(n-1, calculated) + getnthfib2(n-2, calculated)
        return calculated[n]


print("\n")

print(getnthfib2(6))

'''

##############################################################################################################################################################

#https://www.youtube.com/watch?v=BCZWQTY9xPE

#1). write a python program to print prime numbers between 100 and 200.

for num in range(100,200):
    if all(num%i != 0 for i in range(2,num)):
        print(num)


#----------------------------------------------------------------------

#2). write a sort function to sort the elements in a list

my_list = [3,4,1,0,5,2,7,20,15,13,10]
res = []
#first_element = my_list[0]
while my_list:
    first_element = my_list[0]
    for k in my_list:
        if k > first_element:
            first_element = k
    res.append(first_element)
    my_list.remove(first_element)

    
print(res)
#print(my_list.sort(reverse=True))

#----------------------------------------------------------------------

#3). write a Python program to print Fibinacci Series

def getfibs(n):
    if n ==1:
        return 0
    elif n <= 3:
        return 1
    else:
        return getfibs(n-1) + getfibs(n-2)

for k in range(1,20):
    print(getfibs(k))

#-------------------------------------------------------------------------

#4). print a list in reverse

my_list = [3,4,1,0,5,2,7,20,15,13,10]
res = []
for k in range(1, len(my_list)):
    res.append(my_list[len(my_list)-k])

print(res)


#------------------------------------------------------------------------

#5). write a Python program to check whether a string is a palindrome or not (Madam)

def check_pali(stri):
    # check
    revs = stri[::-1]
    if all(stri[k] == revs[k] for k in range(0,len(stri))):
        return  "true"
    else:
        return  "false"


print(check_pali("madam"))
print(check_pali("kavyu"))
print(check_pali("rotator"))

#---------------------------------------------------------------------------------

# 6). write a program to print set of duplicates in a list.

my_list = [3,4,1,0,5,2,7,20,15,13,10,2,3]

print(set([x for x in my_list if my_list.count(x) > 1]))



#----------------------------------------------------------------------------------

# 7). write a program print the number of words in a given sentence.

s = "write a program print the number of words in a given sentence"

print(len(s.split()))

#----------------------------------------------------------------------------------

# 8). Given an array arr[] of n elements, write a function to search a given element x in arr[]

def search(arr,x):
    for i in range(len(arr)):
        if arr[i] == x:
            return i 
    print("Not present in the list") 

listt = [1,2,3,4,4,5,5,6,1,7]   

print(search(listt,4))
print(search(listt,10))
print(search(listt,6))


#--------------------------------------------------------------------------------------

# 9). write a program to implement binary search.

def binary_search(array, target):
    lower = 0
    upper = len(array)

    while lower < upper: 
        x = lower + (upper - lower)//2
        val = array[x]
        if target == val:
            return x
        elif target > val:
            if lower == x:
                break
            lower =x
        elif target < val:
            upper = x

listt = [1,2,3,4,4,5,5,6,1,7]   
print(binary_search(listt, 4))


#-----------------------------------------------------------------------------------------

# 10). write a program to join two strings 

test_string = "STRING ONE"
add_string = " string two"

res = "".join((test_string, add_string))

print("The concatenated string is : " + res)


#------------------------------------------------------------------------------------------

# 11). write a program to extract digits from a given string

test_string = "lw3e4r5t6y7u7i8i"

# extract digit string

res = ''.join(filter(lambda i: i.isdigit(), test_string))
print("The digits string is : " + str(res))


#-----------------------------------------------------------------------------------------

# 12). write a python program to split strings using newline delimiter.

init_str = 'This is a test program'

print("initial string is = ", init_str)
print("Initial string is : = " + init_str)

res_str = (init_str.rstrip().split(' '))

print("Resultant string is = ", str(res_str))
print("Resultant string is : = " + str(res_str))


#----------------------------------------------------------------------------------------

# 13). Given a string as your input, delete any reoccuring character, and return the new string.


def deleteReccurringCharacter(string):
    seenCharacters = set()
    outputString = ''
    for char in string:
        if char not in seenCharacters:
            seenCharacters.add(char)
            outputString += char 
    return outputString 

print(deleteReccurringCharacter("aaaabbbvvvccceee"))



#########################################################################################################################################################################################

#https://www.geeksforgeeks.org/count-possible-paths-top-left-bottom-right-nxm-matrix/

'''
Find all the paths from top left corner to the bottom right corner of the mxn matrix
'''

# TIME COMPLEXITY IS O(mn)

def return_paths(mat):
    r,c = len(mat),len(mat[0])
    for j in range(len(mat[0])):
        mat[0][j] = 1
    for i in range(1,len(mat)):
        mat[i][0] =1
    for i in range(1,len(mat)):
        for j in range(1,len(mat[0])):
            mat[i][j] = mat[i-1][j] + mat[i][j-1]
    #print(mat)
    print(mat[r-1][c-1])
    return mat #[r-1][c-1]

 
#mat = [ [ 0, 0, 0, -1, 0 ], [ -1, 0, 0, -1, -1 ], [ 0, 0, 0, -1, 0 ], [ -1, 0, -1, 0, -1 ], [ 0, 0, -1, 0, 0 ] ]

s = (3,5)
mat = np.zeros(s)

print(return_paths(mat))


# We can reduce the space complexity to O(n)

def return_paths2(mat):
    dp = [1]*len(mat[0])
    for i in range(len(mat)-1):
        for j in range(1,len(mat[0])):
            dp[j] += dp[j-1]
    return dp[len(mat[0])-1]

print(return_paths2(mat))

# we allow diagonal movements


def return_paths3(mat):
    r,c = len(mat),len(mat[0])
    for j in range(len(mat[0])):
        mat[0][j] = 1
    for i in range(1,len(mat)):
        mat[i][0] =1
    for i in range(1,len(mat)):
        for j in range(1,len(mat[0])):
            mat[i][j] = mat[i-1][j] + mat[i][j-1] + mat[i-1][j-1]
    #print(mat)
    print(mat[r-1][c-1])
    return mat #[r-1][c-1]


print("---- return_paths3 -------------------")
mat1 = [[1, 2, 3],
       [4, 5, 6]]
 
return_paths3(mat1)

print("222222222222222222222222222")
mat2 = [[1, 2, 3],
       [4, 5, 6],
       [2, 5, 1]]
 
return_paths3(mat2)

print("333333333333333333333333333")
mat3 = [[1, 2, 3],
       [4, 5, 6],
       [2, 5, 1],
       [0, 1, 5]]
 
return_paths3(mat3)
 
print("---- end of return_paths3 -------------------")

#-----------------------------------------------------------------------------------------------------------------------------------------------------------------

#https://www.geeksforgeeks.org/print-all-possible-paths-from-top-left-to-bottom-right-of-a-mxn-matrix/

# we allow diagonal movements

# Python3 program to Print all possible paths from
# top left to bottom right of a mXn matrix
 
'''
/* mat: Pointer to the starting of mXn matrix
i, j: Current position of the robot
     (For the first call use 0, 0)
m, n: Dimentions of given the matrix
pi: Next index to be filed in path array
*path[0..pi-1]: The path traversed by robot till now
                (Array to hold the path need to have
                 space for at least m+n elements) */
'''
#n_paths =0
def printAllPathsUtil(mat, i, j, path, pi):
    #n_paths =0
    m,n = len(mat), len(mat[0])
    # Reached the bottom of the matrix
    # so we are left with only option to move right
    if (i == m - 1):
        for k in range(j, n):
            path[pi + k - j] = mat[i][k]
 
        for l in range(pi + n - j):
            print(path[l], end = " ")
            #n_paths +=1
        print()
        return
 
    # Reached the right corner of the matrix
    # we are left with only the downward movement.
    if (j == n - 1):
 
        for k in range(i, m):
            path[pi + k - i] = mat[k][j]
 
        for l in range(pi + m - i):
            print(path[l], end = " ")
            #n_paths +=1
        print()
        return
 
    # Add the current cell
    # to the path being generated
    path[pi] = mat[i][j]
 
    # Print all the paths
    # that are possible after moving down
    printAllPathsUtil(mat, i + 1, j, path, pi + 1)
 
    # Print all the paths
    # that are possible after moving right
    printAllPathsUtil(mat, i, j + 1, path, pi + 1)
 
    # Print all the paths
    # that are possible after moving diagonal
    printAllPathsUtil(mat, i+1, j+1, path, pi + 1)
    #print(n_paths)
 
# The main function that prints all paths
# from top left to bottom right
# in a matrix 'mat' of size mXn
def printAllPaths(mat):
 
    path = [0 for i in range(len(mat) + len(mat[0]))]
    printAllPathsUtil(mat, 0, 0, path, 0)
 
# Driver Code
mat1 = [[1, 2, 3],
       [4, 5, 6]]
 
printAllPaths(mat1)

print("222222222222222222222222222")
mat2 = [[1, 2, 3],
       [4, 5, 6],
       [2, 5, 1]]
 
printAllPaths(mat2)

print("333333333333333333333333333")
mat3 = [[1, 2, 3],
       [4, 5, 6],
       [2, 5, 1],
       [0, 1, 5]]
 
printAllPaths(mat3)


#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# put restrictions on the above problem.

def printAllPathsUtil(mat, i, j, path, pi):
    m,n = len(mat), len(mat[0])
    # Reached the bottom of the matrix
    # so we are left with only option to move right
    if (i == m - 1):
        for k in range(j, n):
            if (mat[i][k] != -1):
                path[pi + k - j] = mat[i][k]
            else:
                path[pi + k - j] = ""
 
        for l in range(pi + n - j):
            print(path[l], end = " ")
        print()
        return
 
    # Reached the right corner of the matrix
    # we are left with only the downward movement.
    if (j == n - 1):
 
        for k in range(i, m):
            if(mat[k][j] != -1):
                path[pi + k - i] = mat[k][j] 
            else:
                path[pi + k - i] = ""
 
        for l in range(pi + m - i):
            print(path[l], end = " ")
        print()
        return
 
    # Add the current cell
    # to the path being generated
    if (mat[i][j] != -1):
        path[pi] = mat[i][j]
    else:
        path[pi] = ""
 
    # Print all the paths
    # that are possible after moving down
    printAllPathsUtil(mat, i + 1, j, path, pi + 1)
 
    # Print all the paths
    # that are possible after moving right
    printAllPathsUtil(mat, i, j + 1, path, pi + 1)
 
    # Print all the paths
    # that are possible after moving diagonal
    printAllPathsUtil(mat, i+1, j+1, path, pi + 1)
 
# The main function that prints all paths
# from top left to bottom right
# in a matrix 'mat' of size mXn
def printAllPaths(mat):
    path = [0 for i in range(len(mat) + len(mat[0]))]
    printAllPathsUtil(mat, 0, 0, path, 0)
 
# Driver Code
print("----------- restricted cell entries -------------")
mat1 = [[0, -1, 0],
       [0, 0, 0]]
 
printAllPaths(mat1)

'''
print("222222222222222222222222222")
mat2 = [[0, 0, -1],
       [0, -1, 0],
       [0, 0, 0]]
 
printAllPaths(mat2)

print("333333333333333333333333333")
mat3 = [[0, 0, -1],
       [0, 0,  0],
       [0, -1, 0],
       [0, 0, 0]]
 
printAllPaths(mat3)

'''


#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------

#https://www.geeksforgeeks.org/subset-sum-backtracking-4/?ref=leftbar-rightbar

'''
total_nodes =0
#prints subset found
def printSubset( A, size):
    for i in range(size):
        print(A[i],"")
 
# inputs
# s            - set vector
# t            - tuplet vector
# s_size       - set size
# t_size       - tuplet size so far
# sum          - sum so far
# ite          - nodes count
# target_sum   - sum to be found
def subset_sum(s, t, s_size, t_size, sum,ite, target_sum,total_nodes):
    total_nodes +=1
    if target_sum == sum:
        # we found subset
        printSubset(t,t_size)
        # exclude previously added item and consider next candidate
        subset_sum(s,t,s_size,t_size-1,sum-s[ite],ite+1,target_sum,total_nodes+1)
        return 
    else:
        #generate nodes along the breadth
        for i in range(ite, s_size):
            t[t_size] = s[i]
            #consider next level node (along depth)
            subset_sum(s,t,s_size,t_size+1,sum+s[i],i+1,target_sum, total_nodes+1)
    return total_nodes

#Wrapper to print subsets that sum to target_sum
#input is weights vector and target_sum
def generateSubsets(s,size,target_sum):
    tuplet_vector = [0 for i in range(size)]
    subset_sum(s,tuplet_vector,size,6,0,0,target_sum,0)

weights = [10,7,5,18,12,20,15]
size = 7
generateSubsets(weights, size,35)
print("Nodes generated = ", total_nodes)
 
'''



#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------

#https://www.geeksforgeeks.org/print-all-permutations-of-a-string-in-java/?ref=leftbar-rightbar

'''
# Function to print all the permutations of str
def printPermutn(str,ans):
    #if str is empty
    if(len(str) == 0):
        print(ans + " ")
        return
    else:
        for i in range(len(str)-1):
            # ith character of the string
            ch = str[i]
            # rest of the string after excluding the ith character
            rest = str[:i] + str[-i:]
            #recursive call
            printPermutn(rest,ans+ch)

# Driver code

s = "abb"
printPermutn(s, "")

'''



#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------

#https://www.geeksforgeeks.org/count-possible-paths-two-vertices/?ref=leftbar-rightbar

print("----------count possible paths between two vertices in a graph ------------")
# Python 3 program to count all paths from a source to a destination. A directed graph using adjacency list representation
class Graph:
    def __init__(self, V):
        self.V = V
        self.adj = [[] for i in range(V)]
    def addEdge(self, u, v):
        # Add v to u’s list.
        self.adj[u].append(v)
    # Returns count of paths from 's' to 'd'
    def countPaths(self, s, d):
        # Mark all the vertices as not visited
        visited = [False] * self.V
        # Call the recursive helper function to print all paths
        pathCount = [0]
        self.countPathsUtil(s, d, visited, pathCount)
        return pathCount[0]
    # A recursive function to print all paths from 'u' to 'd'. visited[] keeps track of vertices in current path. 
    # path[] stores actual vertices and path_index is current index in path[]
    def countPathsUtil(self, u, d, visited, pathCount):
        visited[u] = True
        # If current vertex is same as destination, then increment count
        if (u == d):
            pathCount[0] += 1
        # If current vertex is not destination
        else:
            # Recur for all the vertices adjacent to current vertex
            i = 0
            while i < len(self.adj[u]):
                if (not visited[self.adj[u][i]]):
                    self.countPathsUtil(self.adj[u][i], d, visited, pathCount)
                i += 1
     
        visited[u] = False

# Driver Code
if __name__ == '__main__':
 
    # Create a graph given in the above diagram
    g = Graph(4)
    g.addEdge(0, 1)
    g.addEdge(0, 2)
    g.addEdge(0, 3)
    g.addEdge(2, 0)
    g.addEdge(2, 1)
    g.addEdge(1, 3)
 
    s = 2
    d = 3
    print(g.countPaths(s, d))

# space complexity = O(1)
# Time complexity = O(N!)




#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------

#https://www.geeksforgeeks.org/combinational-sum/?ref=leftbar-rightbar

# Python3 program to find all combinations that sum to a given value
def combinationSum(arr, sum):
    ans = []
    temp = []
    # first do hashing nothing but set{} since set does not always sort removing the duplicates using Set and Sorting the List
    arr = sorted(list(set(arr)))
    findNumbers(ans, arr, temp, sum, 0)
    return ans
 
def findNumbers(ans, arr, temp, sum, index):
    if(sum == 0):
        # Adding deep copy of list to ans
        ans.append(list(temp))
        return
       
    # Iterate from index to len(arr) - 1
    for i in range(index, len(arr)):
        # checking that sum does not become negative
        if(sum - arr[i]) >= 0:
            # adding element which can contribute to sum
            temp.append(arr[i])
            findNumbers(ans, arr, temp, sum-arr[i], i)
            # removing element from list (backtracking)
            temp.remove(arr[i])

# Driver Code
arr = [2, 4, 6, 8]
sum = 8
ans = combinationSum(arr, sum)
 
# If result is empty, then
if len(ans) <= 0:
    print("empty")
     
# print all combinations stored in ans
for i in range(len(ans)):
 
    print("(", end=' ')
    for j in range(len(ans[i])):
        print(str(ans[i][j])+" ", end=' ')
    print(")", end=' ')
 


#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------

#https://www.geeksforgeeks.org/program-for-newton-raphson-method/


# Python3 code for implementation of Newton Raphson Method for solving equations
# An example function whose solution is determined using Bisection Method. 
# The function is x^3 - x^2 + 2

print("--------------Newton Raphson Method -------------------------------")
#def func( x ):
#    return x * x * x - x * x + 2
  
# Derivative of the above function  which is 3*x^x - 2*x


#def derivFunc( x ):
#    return 3 * x * x - 2 * x
def derivFunc(f,x):
    h = 0.001
    res = (f(x+h) - f(x))/h
    return res 

# Function to find the root
def newtonRaphson( f,x ):
    error = f(x) / derivFunc(f,x)
    while abs(error) >= 0.0001:
        error = f(x)/derivFunc(f,x)
        # x(i+1) = x(i) - f(x) / f'(x)
        x = x - error
      
    print("The value of the root is : ", "%.4f"% x)
  
# Driver program to test above
x0 = 20 # Initial values assumed

def fun(x):
    #return x * x * x - x * x + 2
    return x * x - 16

newtonRaphson(fun,x0)



#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------

#https://www.geeksforgeeks.org/bubble-sort/

print("---------------- bubble sort -------------------------")

def bubbleSort(arr):
    n = len(arr)
    # Traverse through all array elements
    for i in range(n):
        # Last i elements are already in place
        for j in range(0, n-i-1):
            # traverse the array from 0 to n-i-1, Swap if the element found is greater than the next element
            if arr[j] > arr[j+1] :
                arr[j], arr[j+1] = arr[j+1], arr[j]
  
# Driver code to test above
arr = [64, 34, 25, 12, 22, 11, 90]
  
bubbleSort(arr)
  
print ("Sorted array is:")
for i in range(len(arr)):
    print ("%d" %arr[i]), 



#--------------------------------------------------- BST -----------------------------------------------------------------------------------------------------------------------

#https://www.geeksforgeeks.org/binary-search-tree-set-1-search-and-insertion/

print("----------------- BST -------------------------------------------")
# A utility function to search a given key in BST
def search(root,key):
    # Base Cases: root is null or key is present at root
    if root is None or root.val == key:
        return root
    # Key is greater than root's key
    if root.val < key:
        return search(root.right,key)
    # Key is smaller than root's key
    return search(root.left,key)


# Python program to demonstrate insert operation in binary search tree
# A utility class that represents an individual node in a BST

class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key
 
# A utility function to insert a new node with the given key
def insert(root, key):
    if root is None:
        return Node(key)
    else:
        if root.val == key:
            return root
        elif root.val < key:
            root.right = insert(root.right, key)
        else:
            root.left = insert(root.left, key)
    return root
 
# A utility function to do inorder tree traversal
def inorder(root):
    if root:
        inorder(root.left)
        print(root.val)
        inorder(root.right)
 
 
# Driver program to test the above functions
# Let us create the following BST
#    50
#  /     \
# 30     70
#  / \ / \
# 20 40 60 80
 
r = Node(50)
r = insert(r, 30)
r = insert(r, 20)
r = insert(r, 40)
r = insert(r, 70)
r = insert(r, 60)
r = insert(r, 80)
 
# Print inoder traversal of the BST
inorder(r)

#print(search(r,40))

#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------


#Most famous ones are : KMP (Knuth Morris Pratt) , Rabin Karp and Finite State Automaton.

#https://www.geeksforgeeks.org/c-program-for-kmp-algorithm-for-pattern-searching-2/

#https://www.geeksforgeeks.org/kmp-algorithm-for-pattern-searching/

#https://www.tutorialspoint.com/c-program-for-kmp-algorithm-for-pattern-searching

#https://tutorialspoint.dev/language/c-and-cpp-programs/searching-for-patterns-set-3-rabin-karp-algorithm

#https://www.geeksforgeeks.org/finite-automata-algorithm-for-pattern-searching/

#https://www.geeksforgeeks.org/binary-search-tree-set-1-search-and-insertion/


# ---------------------------------------------------------- KMP - Knuth Morris Pratt ---------------------------------------------------------------------------------------------------------------

'''
# https://www.geeksforgeeks.org/python-program-for-kmp-algorithm-for-pattern-searching-2/

# Python program for KMP Algorithm
def KMPSearch(pat, txt):
    M = len(pat)
    N = len(txt)
  
    # create lps[] that will hold the longest prefix suffix 
    # values for pattern
    lps = [0]*M
    j = 0 # index for pat[]
  
    # Preprocess the pattern (calculate lps[] array)
    computeLPSArray(pat, M, lps)
  
    i = 0 # index for txt[]
    while i < N:
        if pat[j] == txt[i]:
            i += 1
            j += 1
  
        if j == M:
            print "Found pattern at index " + str(i-j)
            j = lps[j-1]
  
        # mismatch after j matches
        elif i < N and pat[j] != txt[i]:
            # Do not match lps[0..lps[j-1]] characters,
            # they will match anyway
            if j != 0:
                j = lps[j-1]
            else:
                i += 1
  
def computeLPSArray(pat, M, lps):
    len = 0 # length of the previous longest prefix suffix
  
    lps[0] # lps[0] is always 0
    i = 1
  
    # the loop calculates lps[i] for i = 1 to M-1
    while i < M:
        if pat[i]== pat[len]:
            len += 1
            lps[i] = len
            i += 1
        else:
            # This is tricky. Consider the example.
            # AAACAAAA and i = 7. The idea is similar 
            # to search step.
            if len != 0:
                len = lps[len-1]
  
                # Also, note that we do not increment i here
            else:
                lps[i] = 0
                i += 1
  
txt = "ABABDABACDABABCABAB"
pat = "ABABCABAB"
KMPSearch(pat, txt)

'''

# -------------------------------------------------------- Rabin Karp algorithm --------------------------------------------------------------------------------------------------------------------

'''
#https://www.geeksforgeeks.org/python-program-for-rabin-karp-algorithm-for-pattern-searching/

# Following program is the python implementation of
# Rabin Karp Algorithm given in CLRS book
  
# d is the number of characters in the input alphabet
d = 256
  
# pat  -> pattern
# txt  -> text
# q    -> A prime number
  
def search(pat, txt, q):
    M = len(pat)
    N = len(txt)
    i = 0
    j = 0
    p = 0    # hash value for pattern
    t = 0    # hash value for txt
    h = 1
  
    # The value of h would be "pow(d, M-1)% q"
    for i in xrange(M-1):
        h = (h * d)% q
  
    # Calculate the hash value of pattern and first window
    # of text
    for i in xrange(M):
        p = (d * p + ord(pat[i]))% q
        t = (d * t + ord(txt[i]))% q
  
    # Slide the pattern over text one by one
    for i in xrange(N-M + 1):
        # Check the hash values of current window of text and
        # pattern if the hash values match then only check
        # for characters on by one
        if p == t:
            # Check for characters one by one
            for j in xrange(M):
                if txt[i + j] != pat[j]:
                    break
  
            j+= 1
            # if p == t and pat[0...M-1] = txt[i, i + 1, ...i + M-1]
            if j == M:
                print "Pattern found at index " + str(i)
  
        # Calculate hash value for next window of text: Remove
        # leading digit, add trailing digit
        if i < N-M:
            t = (d*(t-ord(txt[i])*h) + ord(txt[i + M]))% q
  
            # We might get negative values of t, converting it to
            # positive
            if t < 0:
                t = t + q
  
# Driver program to test the above function
txt = "GEEKS FOR GEEKS"
pat = "GEEK"
q = 101 # A prime number
search(pat, txt, q)

'''

# ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------

#tensorflow
#keras
#spark
#SQL


#------------------------------------------------ BFS - Breadth First Search --------------------------------------------------------------------------------------------------

#https://www.educative.io/edpresso/how-to-implement-a-breadth-first-search-in-python

print("------------ BFS -------------------------------------------")
graph = {
  'A' : ['B','C'],
  'B' : ['D', 'E'],
  'C' : ['F'],
  'D' : [],
  'E' : ['F'],
  'F' : []
}


visited = [] # List to keep track of visited nodes.
queue = []     #Initialize a queue

def bfs(visited, graph, node):
  visited.append(node)
  queue.append(node)

  while queue:
    s = queue.pop(0) 
    print (s, end = " ") 

    for neighbour in graph[s]:
      if neighbour not in visited:
        visited.append(neighbour)
        queue.append(neighbour)

# Driver Code
bfs(visited, graph, 'A')
print()

'''
#https://www.geeksforgeeks.org/breadth-first-search-or-bfs-for-a-graph/

# Python3 Program to print BFS traversal
# from a given source vertex. BFS(int s)
# traverses vertices reachable from s.
import collections
from collections import defaultdict
 
# This class represents a directed graph
# using adjacency list representation
class Graph:
 
    # Constructor
    def __init__(self):
 
        # default dictionary to store graph
        self.graph = defaultdict(list)
 
    # function to add an edge to graph
    def addEdge(self,u,v):
        self.graph[u].append(v)
 
    # Function to print a BFS of graph
    def BFS(self, s):
 
        # Mark all the vertices as not visited
        visited = [False] * (max(self.graph) + 1)
 
        # Create a queue for BFS
        queue = []
 
        # Mark the source node as
        # visited and enqueue it
        queue.append(s)
        visited[s] = True
 
        while queue:
 
            # Dequeue a vertex from
            # queue and print it
            s = queue.pop(0)
            print (s, end = " ")
 
            # Get all adjacent vertices of the
            # dequeued vertex s. If a adjacent
            # has not been visited, then mark it
            # visited and enqueue it
            for i in self.graph[s]:
                if visited[i] == False:
                    queue.append(i)
                    visited[i] = True
 
# Driver code
 
# Create a graph given in
# the above diagram
g = Graph()
g.addEdge(0, 1)
g.addEdge(0, 2)
g.addEdge(1, 2)
g.addEdge(2, 0)
g.addEdge(2, 3)
g.addEdge(3, 3)
 
print ("Following is Breadth First Traversal"
                  " (starting from vertex 2)")
g.BFS(2)

'''

#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------

#https://www.geeksforgeeks.org/check-possible-path-2d-matrix/

'''

Given a 2D array(m x n). The task is to check if there is any path from top left to bottom right. In the matrix, -1 is considered as blockage (can’t go through this cell)
and 0 is considered path cell (can go through it).

'''
print(" --------- 2d matrix paths again ? ---------------------")

# Python3 program to find if there is path from top left to right bottom
row = 5
col = 5
# to find the path from top left to bottom right
def isPath(arr) :
    # directions
    Dir = [ [0, 1], [0, -1], [1, 0], [-1, 0]]
    # queue
    q = []
    # insert the top right corner.
    q.append((0, 0))
    # until queue is empty
    while(len(q) > 0) :
        p = q[0]
        q.pop(0)
        # mark as visited
        arr[p[0]][p[1]] = -1
        # destination is reached.
        if(p == (row - 1, col - 1)) :
            return True
             
        # check all four directions
        for i in range(4) :
         
            # using the direction array
            a = p[0] + Dir[i][0]
            b = p[1] + Dir[i][1]
             
            # not blocked and valid
            if(a >= 0 and b >= 0 and a < row and b < col and arr[a][b] != -1) :           
                q.append((a, b))
    return False
   
# Given array
arr = [ [ 0,  0,  0, -1,  0 ],
        [ -1, 0,  0, -1, -1 ],
        [ 0,  0,  0,  0,  0 ],
        [ -1, 0, -1,  0,  0 ],
        [ 0,  0, -1,  0,  0 ] ]
 
# path from arr[0][0] to arr[row][col]
if (isPath(arr)) :
    print("Yes")
else :
    print("No")
 
    # This code is contributed by divyesh072019


q = []
q.append((0,0))
p = q[0]
print("q = ", q)
print("q[0] = ", q[0])
print("p = ", p)
print("p[0] = ", p[0])
print("p[1] = ", p[1])

#Time Complexity: O(R*C). 
#Every element of the matrix can be inserted once in the queue, so time Complexity is O(R*C).
#Space Complexity: O(R*C). 
#To store all the elements in a queue O(R*C) space is needed.

print(" ------------ method 2 ----------------------------------")

# Python3 program to find if there
# is path from top left to right bottom
row = 5
col = 5
 
# to find the path from
# top left to bottom right
def isPath(arr):
     
    # set arr[0][0] = 1
    arr[0][0] = 1
 
    # Mark reachable (from top left)
    # nodes in first row and first column.
    for i in range(1, row):
        if (arr[i][0] != -1):
            arr[i][0] = arr[i-1][0]
 
    for j in range(1, col):
        if (arr[0][j] != -1):
            arr[0][j] = arr[0][j-1]
             
    # Mark reachable nodes in
    # remaining matrix.
    for i in range(1, row):
        for j in range(1, col):
            if (arr[i][j] != -1):
                arr[i][j] = max(arr[i][j - 1], arr[i - 1][j])
                                 
    # return yes if right
    # bottom index is 1
    return (arr[row - 1][col - 1] == 1)
 
# Driver Code
 
# Given array
arr = [[ 0, 0, 0, -1, 0 ],
       [-1, 0, 0, -1, -1],
       [ 0, 0, 0, -1, 0 ],
       [-1, 0, -1, 0, -1],
       [ 0, 0, -1, 0, 0 ]]
 
# path from arr[0][0] to arr[row][col]
if (isPath(arr)):
    print("Yes")
else:
    print("No")


#Time Complexity: O(R*C). 
#Every element of the matrix is traversed, so time Complexity is O(R*C).
#Space Complexity: O(1). 
#No extra space is needed.   


#--------------------------------------------------------------------------------------------------------------------------

print("--------- Bloomberg interview 2 -----------------------------")

res = [(0,3),(1,2),(2,5),(3,1),(4,4)]
print(res)
print()
print(res[:3])
print()
res2 = [i[0] for i in res]
print(res2[:3])

"""
Given a m * n matrix mat of ones (representing soldiers) and zeros (representing civilians), return the indexes of the
k weakest rows in the matrix ordered from the weakest to the strongest.

A row i is weaker than row j, if the number of soldiers in row i is less than the number of soldiers in row j, or they
have the same number of soldiers but i is less than j. Soldiers are always stand in the frontier of a row, that is,
always ones may appear first and then zeros.

Input: mat =
[[1,1,0,0,0],
 [1,1,1,1,0],
 [1,0,0,0,0],
 [1,1,0,0,0],
 [1,1,1,1,1]],
k = 3
Output: [2,0,3]
Explanation:
The number of soldiers for each row is:
row 0 -> 2
row 1 -> 4
row 2 -> 1
row 3 -> 2
row 4 -> 5
Rows ordered from the weakest to the strongest are [2,0,3,1,4]

Input: mat =
[[1,0,0,0],
 [1,1,1,1],
 [1,0,0,0],
 [1,0,0,0]],

k = 2
Output: [0,2]
Explanation:
The number of soldiers for each row is:
row 0 -> 1
row 1 -> 4
row 2 -> 1
row 3 -> 1
Rows ordered from the weakest to the strongest are [0,2,3,1]
"""


class Solution:
    def kWeakestRows(self, mat, k):
        #pass
        res = []
        for j in range(len(mat)):
            # j -> index
            res.append((j,np.sum(mat[j])))
        # res = [(0, sum()), () ..., ()]
        res.sort(key=lambda x:x[1])
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

#---------------------------------------------- print all paths from a node to a parent node ---------------------------------------------------------------------------------

#https://www.geeksforgeeks.org/find-paths-given-source-destination/

#Given acyclic graph find all the paths to a node from a parent node.
#Print all paths from a given source to a destination

# Python program to print all paths from a source to destination.
   
from collections import defaultdict
   
# This class represents a directed graph 
# using adjacency list representation
class Graph:
   
    def __init__(self, vertices):
        # No. of vertices
        self.V = vertices 
        # default dictionary to store graph
        self.graph = defaultdict(list) 
   
    # function to add an edge to graph
    def addEdge(self, u, v):
        self.graph[u].append(v)
   
    #A recursive function to print all paths from 'u' to 'd'.
    #visited[] keeps track of vertices in current path. path[] stores actual vertices and path_index is current index in path[]
    
    def printAllPathsUtil(self, u, d, visited, path):
  
        # Mark the current node as visited and store in path
        visited[u]= True
        path.append(u)
        # If current vertex is same as destination, then print current path[]
        if u == d:
            print(path)
        else:
            # If current vertex is not destination Recur for all the vertices adjacent to this vertex
            for i in self.graph[u]:
                if visited[i]== False:
                    self.printAllPathsUtil(i, d, visited, path)          
        # Remove current vertex from path[] and mark it as unvisited
        path.pop()
        visited[u]= False
   
   
    # Prints all paths from 's' to 'd'
    def printAllPaths(self, s, d):
        # Mark all the vertices as not visited
        visited =[False]*(self.V)
        # Create an array to store paths
        path = []
        # Call the recursive helper function to print all paths
        self.printAllPathsUtil(s, d, visited, path)
   

# Create a graph given in the above diagram
g = Graph(4)
g.addEdge(0, 1)
g.addEdge(0, 2)
g.addEdge(0, 3)
g.addEdge(2, 0)
g.addEdge(2, 1)
g.addEdge(1, 3)
   
s = 2 ; d = 3
print("Following are all different paths from % d to % d :" %(s, d))
g.printAllPaths(s, d)


#Time Complexity: O(V^V). 
#The time complexity is polynomial. From each vertex there are v vertices that can be visited from current vertex.
#Auxiliary space: O(V^V). 
#To store the paths V^V space is needed.

# ------------------------------------------------------------ BFS for shortest path -----------------------------------------------------------------------------------------------------------

#https://www.geeksforgeeks.org/building-an-undirected-graph-and-finding-shortest-path-using-dictionaries-in-python/

# Python3 implementation to build a graph using Dictonaries
  
from collections import defaultdict
# Function to build the graph
def build_graph():
    edges = [
        ["A", "B"], ["A", "E"], 
        ["A", "C"], ["B", "D"],
        ["B", "E"], ["C", "F"],
        ["C", "G"], ["D", "E"]
    ]
    graph = defaultdict(list)
      
    # Loop to iterate over every edge of the graph
    for edge in edges:
        a, b = edge[0], edge[1]
          
        # Creating the graph as adjacency list
        graph[a].append(b)
        graph[b].append(a)
    return graph
  
if __name__ == "__main__":
    graph = build_graph()
    print(graph)

# Python implementation to find the shortest path in the graph using dictionaries 
# Function to find the shortest path between two nodes of a graph

def BFS_SP(graph, start, goal):
    explored = [] 
    # Queue for traversing the graph in the BFS
    queue = [[start]]
      
    # If the desired node is  reached
    if start == goal:
        print("Same Node")
        return
      
    # Loop to traverse the graph 
    # with the help of the queue
    while queue:
        path = queue.pop(0)
        node = path[-1]
          
        # Codition to check if the
        # current node is not visited
        if node not in explored:
            neighbours = graph[node]
              
            # Loop to iterate over the 
            # neighbours of the node
            for neighbour in neighbours:
                new_path = list(path)
                new_path.append(neighbour)
                queue.append(new_path)
                  
                # Condition to check if the 
                # neighbour node is the goal
                if neighbour == goal:
                    print("Shortest path = ", *new_path)
                    return
            explored.append(node)
  
    # Condition when the nodes 
    # are not connected
    print("So sorry, but a connecting"\
                "path doesn't exist :(")
    return
  
# Driver Code
if __name__ == "__main__":
      
    # Graph using dictionaries
    graph = {'A': ['B', 'E', 'C'],
            'B': ['A', 'D', 'E'],
            'C': ['A', 'F', 'G'],
            'D': ['B', 'E'],
            'E': ['A', 'B', 'D'],
            'F': ['C'],
            'G': ['C']}
      
    # Function Call
    BFS_SP(graph, 'A', 'D')




# ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------



'''
################################################################################################################


Application
I interviewed at Bloomberg L.P.

Interview
takes two months, two rounds of tech phone interviews, one round of hr interview, one tech interview is on your project and coding, other is open problem, 
designing a classifier

Interview Questions
your projects

################################################################################################################


Application
I applied through college or university. I interviewed at Bloomberg L.P. in Feb 2018

Interview
On campus interview. First round has 3 coding problems and ask for some knowledge about machine learning like SVM and NLP. Second round contains some questions 
about the projects and design a data driven method to increase subscibers.

Interview Questions
Matrix Path
BST add sibling



################################################################################################################


Application
I applied online. The process took 2 months. I interviewed at Bloomberg L.P.

Interview
Scheduled for an interview. Recruiter said an interview scheduled but never responded with what type of interview it is. I was expecting questions related to machine 
Learning and not coding, but at the end it was a coding interview. started with what I do now and then a coding question. I could not finish on time :(

Interview Questions
Given acyclic graph find all the paths to a node from a parent node.


################################################################################################################

Application
I applied through a recruiter. The process took 2 months. I interviewed at Bloomberg L.P. (New York, NY) in Oct 2017

Interview
I was contacted by a recruiter who managed the process from the beginning to end. There were 2 phone screens, one on general technical questions based on algorithms and data structures 
and the other was fully focused on machine learning fundamentals. The phone screens were conducted within a gap of two weeks according to the dates made available by me. The interviewers 
were very nice and helpful. After I got selected for the phone screen, I had to travel to NYC for an onsite interview. There were 5 onsite interviews. All the interviewers came in pairs. 
One of the interview was taken by the hiring manager and the team leader. There was also a full HR interview. All the other interviews were conducted by either the team members or team members 
from the data science team with which the machine learning engineers closely work with. All of them were very nice and give directions when I was going away from the right solutions.
 Right after a day of the interview, the recruiter called me to let me know that I have an offer. Within 2 days I got the final offer via email. The entire process was very smooth and I should say awesome.

Interview Questions
Apart from the rounds with the hiring manager and HR, all the rounds were focused on data structure and algorithm problems from Leetcode (Medium and Hard). If someone is prepared thoroughly,
 he should be able to answer most of the questions. The other type of questions were on machine learning fundamentals, models, and open-ended questions of machine learning system design. 
 The manager and HR did ask behavioral questions related to team work, working in agile methodology and also how to tackle difficult challenges.

'''

##################################################################################################################










print("######################################################### ML projects ##############################################################################################")

import numpy as np
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
#importing dataset
import sklearn
from sklearn import svm, datasets
#from sklearn.cross_validation import train_test_split
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score
from sklearn.metrics import confusion_matrix

from sklearn.datasets import load_iris
from sklearn import tree
#X, y = load_iris(return_X_y=True)
#splitting the dataset
#X_train, Y_train, X_test, Y_test = train_test_split(X,y, test_size = 0.2)
iris = datasets.load_iris()
df = pd.DataFrame(iris.data, columns=iris.feature_names)
df['species'] = np.array([iris.target_names[i] for i in iris.target])

X_train, X_test, y_train, y_test = train_test_split(df[iris.feature_names], iris.target, test_size=0.2, stratify=iris.target, random_state=123456)


# DECISION TREE
DT_clf = tree.DecisionTreeClassifier()
DT_clf = DT_clf.fit(X_train, y_train)
predictions = DT_clf.predict(X_test)
print(accuracy_score(y_test, predictions))

# RANDOM FOREST
from sklearn.ensemble import RandomForestClassifier
#iris = datasets.load_iris()
#df = pd.DataFrame(iris.data, columns=iris.feature_names)
#df['species'] = np.array([iris.target_names[i] for i in iris.target])

#X_train, X_test, y_train, y_test = train_test_split(df[iris.feature_names], iris.target, test_size=0.2, stratify=iris.target, random_state=123456)

rf = RandomForestClassifier(n_estimators=100, oob_score=True, random_state=123456)
rf.fit(X_train, y_train)
predicted = rf.predict(X_test)
accuracy = accuracy_score(y_test, predicted)
print(accuracy)

cm = pd.DataFrame(confusion_matrix(y_test, predicted), columns=iris.target_names, index=iris.target_names)
print(sns.heatmap(cm, annot=True))
print(cm)

# LOGISTIC REGRESSION
from sklearn.linear_model import LogisticRegression
logreg = LogisticRegression(C=1e-5)
logreg.fit(X_train, y_train)
preds = logreg.predict(X_test)
print("logistic regression accuracy = ", accuracy_score(y_test, preds))


# SUPPORT VECTOR MACHINES
C = 1.0  # SVM regularization parameter
models = svm.SVC(kernel='rbf', gamma=0.7, C=C)
models.fit(X_train, y_train)
preds2 = models.predict(X_test)
print("RBF svm accuracy = ", accuracy_score(y_test, preds2))




#################################################################################################################################################################################
