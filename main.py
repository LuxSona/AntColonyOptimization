from ACO import ACO
from TSP import TravellingSalesmanProblem
import numpy as np 
from utils import load_coordinates_from_file
import json

def main():

    with open("arguments.json") as fp:
        parameters = json.load(fp)

    #Load parameters into the namespace
    filename : str = parameters["filename"]
    n_ants : int = parameters["n_ants"]
    pheromone_weight : float = parameters["pheromone_weight"]
    heuristic_weight : float = parameters["heuristic_weight"]
    evaporation_rate : float = parameters["evaporation_rate"]
    Q : float = parameters["Q"]
    coordinates, labels = load_coordinates_from_file(filename)
    
    problem = TravellingSalesmanProblem(labels, coordinates)
    
    optimization = ACO(
        problem,
        n_ants=n_ants,
        pheromone_weight=pheromone_weight,
        heuristic_weight=heuristic_weight,
        evaporation_rate=evaporation_rate,
        Q=Q
    )
    
    path, length = optimization.iterate(500)
    for item in path:
        fro, to = item
        print(f"{problem.indices_to_labels[fro]} -> {problem.indices_to_labels[to]}")
    print(f"Total Length: {length}")


if __name__ == "__main__":
    main()
