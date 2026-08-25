from ACO import ACO
from TSP import TravellingSalesmanProblem
from utils import load_coordinates_from_file
import json

def main():

    with open("arguments.json", 'r', encoding='utf-8') as fp:
        parameters = json.load(fp)

    #Load parameters into the namespace
    filename : str = parameters["filename"]
    n_ants : int = parameters["n_ants"]
    pheromone_weight : float = parameters["pheromone_weight"]
    heuristic_weight : float = parameters["heuristic_weight"]
    evaporation_rate : float = parameters["evaporation_rate"]
    Q : float = parameters["Q"]
    iterations: int = parameters["iterations"]
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

    path, length = optimization.iterate(iterations)
    verbose_path : list[str] = []
    for item in path:
        _, to = item
        verbose_path.append(problem.indices_to_labels[to])
    print(verbose_path, length)


if __name__ == "__main__":
    main()
