# Artificial Intelligence Nanodegree
## Introductory Project: Diagonal Sudoku Solver

# Question 1 (Naked Twins)
Q: How do we use constraint propagation to solve the naked twins problem?  
A: 

Assuming I understand the term 'constraint propagation' correcty, which means to use constraints to narrow down the correct answer to a variable, which can narrow down the the choices for other variable. A naked twin problem presents a unit (row, column, or square) with two boxes, each containing both numbers. It can be reasoned that those two numbers then MUST be in those two boxes, and its presence outside those two boxes are not possible. Thus, we can elimite those two numbers from other boxes in the unit. 

# Question 2 (Diagonal Sudoku)
Q: How do we use constraint propagation to solve the diagonal sudoku problem?  
A: 

The diagonal sudoku problem adds more more type of constraint to the sudoku, which is that diagnoal boxes of length 9 form a unit. The original elimination and only-choice strategies are both defined to take units constraint into consideration, via the concept of units and peers. 


### Install

This project requires **Python 3**.

We recommend students install [Anaconda](https://www.continuum.io/downloads), a pre-packaged Python distribution that contains all of the necessary libraries and software for this project. 
Please try using the environment we provided in the Anaconda lesson of the Nanodegree.

##### Optional: Pygame

Optionally, you can also install pygame if you want to see your visualization. If you've followed our instructions for setting up our conda environment, you should be all set.

If not, please see how to download pygame [here](http://www.pygame.org/download.shtml).

### Code

* `solutions.py` - You'll fill this in as part of your solution.
* `solution_test.py` - Do not modify this. You can test your solution by running `python solution_test.py`.
* `PySudoku.py` - Do not modify this. This is code for visualizing your solution.
* `visualize.py` - Do not modify this. This is code for visualizing your solution.

### Visualizing

To visualize your solution, please only assign values to the values_dict using the ```assign_values``` function provided in solution.py

### Data

The data consists of a text file of diagonal sudokus for you to solve.
