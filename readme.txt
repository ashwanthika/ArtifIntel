NAME: ASHWANTHIKA UMASANKAR
UTA ID: 1001854976 
AI ASSIGNMENT 1


The following file is the description for the code named "find_route".
The code contians the following functions:
 
def read: This method reads the the input.txt file with various sources and destinations. It stores them in a list, that contains source, destination and cost
def hue_read: if heuristic values are given, this function is used  
def Uniform_astar: Performs the uniform cost serach or calls the add heuristic method that will help in performing the A-star search
def addHeuristic: contains method that helps in performing astar search 
def expand: It has the expand function that helps in expaning a articular node and adding them to the fringe. 
def route: Once the goal is reached, the optimal path is got by back tracing and this function backtraces and gets us the path. 


NOTE: IF the code is compiled in ide's like spyder, the console might show "List index out of range". PLEASE IGNORE that and proceed to run in the cmd.
 That message is because there is no element in the fringe during the start. Please proceed to run the code in cmd and the output will come. 


The python file name is called find_route.py. 

For UCS Implementation:  py find_route.py input1.txt source destination
			(OR)
			python find_route.py input1.txt source destination

For A* Implementation :  py find_route.py input1.txt source destination  h_kassel.txt
			(OR)
			python find_route.py input1.txt source destination  h_kassel.txt

All the input text files should be included in the same folder

Language: Python

Version : 3.7.4

Note : The source and destination is case sensitive please do check the input file 
