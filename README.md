# 8 Puzzle Solver for Image and Number Using A *

[Jan 2021]<br>
This repository contains an implementation of the A* algorithm applied to solve the classic 8-Puzzle problem. The A* algorithm is an informed search algorithm that intelligently explores the search space by combining the cost to reach the current state and a heuristic estimate of the remaining cost to the goal state.

## Features
<ul>
<li><b>Heuristic-driven Optimization:</b> A* intelligently explores possible solutions by considering both the actual cost and a heuristic estimate.

<li><b>Versatility:</b> Solve the 8-Puzzle problem with either numbers or images, showcasing the adaptability of the AI algorithm.

<li><b>Visual Representation:</b> Visualize the steps taken to solve image-based puzzles, with an option to save the intermediate results.
</ul>

## Getting Started

### Pre-requisites
<ul>
  <li> Python 3.x</li>
  <li> OpenCV </li>
</ul>

### Installation
<b>1. Clone the repository:</b>
<br>git clone https://github.com/yourusername/AI-Puzzle-Solver.git

<b>2. Navigate to Project Directory:</b>
<br>cd AI-Puzzle-Solver

<b>3. Install dependencies</b>
<br>pip install opencv-python
<br>pip install numpy

### Usage
Run the 'main.py' file:
<be>
<br>python  main.py

Follow the on-screen instructions

## A* Algorithm
The A* algorithm uses a combination of the actual cost to reach a node (g) and a heuristic estimate of the remaining cost to the goal (h). The total cost (f) is given by:
<br> f(x) = g(x) + h(x)
<br>In the context of the 8-Puzzle, the heuristic function 'h(x)' calculates the number of misplaced tiles between the current state and the goal state.

## Results

#### Step 0 - Inital Stage<br>

<img src="https://github.com/jayant1211/8-puzzle-Image-Number/blob/main/Results/1.JPG" width="75%" height="75%">

#### Step 1<br>

<img src="https://github.com/jayant1211/8-puzzle-Image-Number/blob/main/Results/2.JPG" width="75%" height="75%">

#### Step 2<br>

<img src="https://github.com/jayant1211/8-puzzle-Image-Number/blob/main/Results/3.JPG" width="75%" height="75%">

<be>
<br>
<img src="https://github.com/jayant1211/8-puzzle-Image-Number/blob/main/Results/res.JPG" width="75%" height="75%">


