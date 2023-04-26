# 8 Puzzle Solver for Image and Number Using A *

[Jan 2021]<br>
The 8 puzzle, also known as the sliding puzzle or tile puzzle, is a classic puzzle consisting of eight sliding tiles on a 3x3 grid. The tiles are numbered from 1 to 8, with one tile missing. The objective of the puzzle is to rearrange the tiles into their correct order by sliding them horizontally or vertically into the empty space, with the goal of achieving the lowest number of moves possible.<br>
A* is a popular pathfinding algorithm used to find the shortest path between two points in a graph or a grid. It combines elements of Dijkstra's algorithm and heuristics to find the shortest path quickly and efficiently. The algorithm uses a priority queue to explore the graph by choosing the next best node to expand based on the estimated total cost of the path from the starting node to the destination node. The heuristic function is an essential component of A*. It estimates the cost of the path from a current node to the goal node and uses this value to prioritize the search and expand nodes that are more likely to lead to the goal.

This project uses A* algo to solve the 8 puzzle, either for number or for an image, choice is prompted after running <i>main.py</i>. If user selects image, we ask path for that image, and we ask jumbled matrix(considering 1 is correct top-left corner of image, 2 is middle in 1st row etc.), which represents the puzzle to solve.

### Requirements
<ul>
<li> OpenCV
<li> NumPy
</ul>


### Results

After giving input for puzzled matrix of image:

Step 0 - Inital Stage<br>

<img src="https://github.com/jayant1211/8-puzzle-Image-Number/blob/main/Results/1.JPG" width="50%" height="50%">

Step 1<br>

<img src="https://github.com/jayant1211/8-puzzle-Image-Number/blob/main/Results/2.JPG" width="50%" height="50%">

Step 2<br>

<img src="https://github.com/jayant1211/8-puzzle-Image-Number/blob/main/Results/3.JPG" width="50%" height="50%">

Result <br>

<img src="https://github.com/jayant1211/8-puzzle-Image-Number/blob/main/Results/res.JPG" width="50%" height="50%">
