# Ant Colony Optimization
This repository implements the Ant Colony Optimization strategy for the Travelling Salesman Problem (TSP). 

# Description 
The Travelling Salesman Problem is a famous computer science problem which involves answering the question: "Given a list of locations on a graph, what is the shortest path which visits all cities?"

The path is famously NP Complete, which means that producing an optimal solution becomes intractable as the size of the input (in this case, the number of nodes in our graph) increases.

The Ant Colony Optimization strategy aims to produce an approximately optimal (i.e. not the best, but a sufficiently decent) solution relatively quickly.

It does so by simulating ant behavior. The strategy simulates a number of ants at random nodes within our graph. Then, each ant may select an edge to travel across based off of the amount of pheromone on that edge AND the weight of that edge. Upon selecting an edge, the ant "travels" across the edge, depositing an amount of pheromone.

As the number of iterations increase, the approximate solution produced approaches the optimal solution. 
## Hyperparameters
To run the Ant Colony Optimization algorithm, we must consider a number of hyperparameters
* **N:** Represents the number of ants which the computer simulates
* **Pheromone Weight:** Also called **α**. It represents the importance an ant gives to pheromones when selecting an edge.
* **Heuristic Weight:** Also called **β**, It represents the importance an ant gives to a heuristic (e.g. the distance between two locations) when selecting the edges.
* **Evaporation Rate:** Also called **ρ**. It represents the evaporation rate of a pheromone for each iteration.
* **Q:** Determines the total amount of pheromone deposited on each edge.
# Getting Started
## Dependencies
* Python
* numpy
## Installing
* Clone the repository to your machine.
```bash
git clone git@github.com:LuxSona/AntColonyOptimization.git
```
## Creating a Graph
In order to create a graph to run the optimization on, you will need a list of labels and a list of coordinates at each label point.
The optimization will accept any number of coordinates. 

* Create a text file, preferably within the repository under `graphs/coordinate_graphs`. Name the file anything you'd like.
* For each line, write the name of your location, followed by a list of numbers representing the coordinates. 
* Save your file and update the filename value in `arguments.json` to reflect the path to your new file.
## Running The Program

Edit `arguments.json` and update your hyperparameters and filepath as necessary. Then, when you're ready, run
`python main.py`. The program will output to stdout a human readable path that *should* be approximately optimal, alongside the optimal length.

# Built With
* Python
* Numpy

# Version History
* 0.1.0
** Initial Release

# Disclosures 
A **Large Language Model** was *consulted* during the writing of this repository to aid in some debugging. *However*, at no point was any code generated. All code and text written in this repository is entirely human authored. The author takes full responsibility for the code provided. The precise model used was Anthropic's *Sonnet 5* model.
