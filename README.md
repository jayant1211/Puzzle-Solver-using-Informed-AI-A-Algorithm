# Puzzle Solver using Informed AI - A* Algorithm

This project contains an implementation of the A* algorithm applied to solve the classic 8-Puzzle problem. 

## Features
<ul>
<li><b>Heuristic-driven Optimization:</b> A* intelligently explores possible solutions by considering both the actual cost and a heuristic estimate.

<li><b>Versatility:</b> Solve the 8-Puzzle problem with either numbers or images, showcasing the adaptability of the AI algorithm.

<li><b>Visual Representation:</b> Visualize the steps taken to solve image-based puzzles, with an option to save the intermediate results.
</ul>


### Pre-requisites
<ul>
  <li> Python 3.x</li>
  <li> OpenCV </li>
</ul>

### Installation
<b>1. Clone the repository:</b>
```bash
git clone https://github.com/yourusername/AI-Puzzle-Solver.git
```

<b>2. Navigate to Project Directory:</b>
<br>cd AI-Puzzle-Solver

<b>3. Install dependencies</b>
```bash
pip install opencv-python
```

```bash
pip install numpy
```

### Usage
Run the 'main.py' file:
<be>
```bash
python main.py
```
Select Between Numbered Sliding Puzzle and Sliding Puzzle from an Image. 

If you chose numbered sliding puzzle, you can input a randomized sequence of number for 8-Puzzle. 
For eg.
|      |      |      |
|------|------|------|
| 1    | 2    | 3    |
| _    | 4    | 6    |
| 7    | 5    | 8    |

and after providing the input, you will be prompter to provide goal state, which for this case ideally would be

|      |      |      |
|------|------|------|
| 1    | 2    | 3    |
| 4    | 5    | 6    |
| 7    | 8    | _    |

The A* algorithm uses a combination of the actual cost to reach a node (g) and a heuristic estimate of the remaining cost to the goal (h). 

The total cost (f) is given by:
<br> f(x) = g(x) + h(x)

In the context of the 8-Puzzle, the heuristic function 'h(x)' calculates the number of misplaced tiles between the current state and the goal state.

Here is an representation for working of A* Algo on numbered puzzle:
![A* Pathfinding Algorithm Visualization](resources/A-star%20working.jpg "A* Algorithm in Action")

If you happen to select the image puzzle, you will be prompted to provide the path of the image. You can create jumbled image puzzle by providing sequence.

For eg:
Input image:
![Dog](resources/image.jpeg "Dog")

Jumbled image using user input:
![Dog](resources/grid_intial.jpg "Jumbled State")

Algo will solve for goal state:
![Dog](resources/grid_goal.jpg "Goal State")


## Results
<div style="display: flex; flex-direction: row; justify-content: center; gap: 30px;">
    <img src="resources/input.png" alt="Jumbled Image" title="Initial Image" width="45%"/>
    <img src="resources/jumbled.png" alt="Jumbled Image" title="Jumbled Image" width="45%"/>
</div>
<p align="center">Input & Jumbled Image</p>

**Solving:**
<div style="display: flex; flex-direction: row; justify-content: center; gap: 20px;">
  <img src="resources/step1.png" alt="Step 1" width="75%" height="50"/>
  <img src="resources/step1_.png" alt="Step 1 continued" width="40%"/>
</div>
<p align="center"><em>Step 1</em></p>

<div style="display: flex; flex-direction: row; justify-content: center; gap: 20px;">
  <img src="resources/step2.png" alt="Step 2" width="70%" height="50"/>
  <img src="resources/step2_.png" alt="Step 2 continued" width="40%"/>
</div>
<p align="center"><em>Step 2</em></p>

<div style="display: flex; flex-direction: row; justify-content: center; gap: 20px;">
  <img src="resources/step3.png" alt="Step 3" width="70%" height="50"/>
  <img src="resources/step3_.png" alt="Step 3 continued" width="40%"/>
</div>
<p align="center"><em>Step 3</em></p>

<img src="resources/step4.png" alt="Final"/>
