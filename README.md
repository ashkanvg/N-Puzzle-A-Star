# N-Puzzle with A* Algorithm
**Solving the sliding puzzle using a basic AI algorithm.**

Implement informed search (A*) to solve N-Puzzle. In this file, I want to explain the algorithm and the way my code will work.


## A* Algorithm in AI

It is a searching algorithm that is used to find the shortest path between an initial and a final point.

A* is a computer algorithm that is widely used in pathfinding and graph traversal, the process of plotting an efficiently traversable path between multiple points, called nodes. Noted for its performance and accuracy, it enjoys widespread use.  

The key feature of the A* algorithm is that it keeps a track of each visited node which helps in ignoring the nodes that are already visited, saving a huge amount of time. It also has a list that holds all the nodes that are left to be explored and it chooses the most optimal node from this list, thus saving time not exploring unnecessary or less optimal nodes.

A heuristic algorithm sacrifices optimality, with precision and accuracy for speed, to solve problems faster and more efficiently.

All graphs have different nodes or points which the algorithm has to take, to reach the final node. The paths between these nodes all have a numerical value, which is considered as the weight of the path. The total of all paths transverse gives you the cost of that route.

Initially, the Algorithm calculates the cost to all its immediate neighboring nodes, n, and chooses the one incurring the least cost. This process repeats until no new nodes can be chosen and all paths have been traversed. Then, you should consider the best path among them. If f(n) represents the final cost, then it can be denoted as :

**f(n) = g(n) + h(n),** where :
 - **g(n) =** cost of traversing from one node to another. This will vary from node to node
 -    **h(n) =** heuristic approximation of the node's value. This is not a real value but an approximation cost

## N-Puzzle / Sliding Puzzle

[**N-Puzzle**](https://en.wikipedia.org/wiki/15_puzzle)  or  **sliding puzzle**  is a popular puzzle that consists of N tiles where N can be 8, 15, 24, and so on. 
N-Puzzle will have sqrt(N+1) rows and sqrt(N+1) columns. Eg. 15-Puzzle will have 4 rows and 4 columns and an 8-Puzzle will have 3 rows and 3 columns. 
The puzzle consists of N tiles and **one empty space** where the tiles can be moved. 
Start and Goal configurations (also called state) of the puzzle are provided. The puzzle can be solved by moving the tiles one by one in the single empty space and thus achieving the Goal configuration.

### Initial State
Users will enter their initial state and write "_" as empty space.

### Goal State
The goal state is where all of the numbers be on their places and the empty space placed on the last place of the puzzle.

    1 2 3
    4 5 6
    7 8 _

## A* and 8-Puzzle
We need to calculate f-value in each step to find the goal state. As we mentioned before, f(x) = g(x)+h(x), where:
**g(x) =** the number of nodes traversed from a start node to get to the current node.
**h(x) =** the number of misplaced tiles by comparing the current state and the goal state

### How A* solves the 8-Puzzle problem?
We first move the empty space in all the possible directions in the start state and calculate the  **f-score** for each state. This is called expanding the current state.  

After expanding the current state, it is pushed into the  **closed**  list and the newly generated states are pushed into the  **open**  list. A state with the least f-score is selected and expanded again. This process continues until the goal state occurs as the current state. Basically, here we are providing the algorithm a measure to choose its actions. The algorithm chooses the best possible action and proceeds in that path.  

This solves the issue of generating redundant child states, as the algorithm will expand the node with the least  **f-score**.

## Inputs
At firs the user should write the size of the puzzle. 
if it is N-Puzzle, they should enter sqrt(N+1).

    3

Then, after that they should input the initial state. eg:

    1 2 3
    4 5 6
    7 _ 8

## Output
The algorithm would work in a proper way and each step would display in terminal. 
Also, in every step the code would display the f-value of that state.
