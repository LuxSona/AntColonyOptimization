from ACO import ACO
from TSP import TravellingSalesmanProblem
import numpy as np 
from utils import load_coordinates_from_file

def main():
    cities = {
        "Albuquerque": np.array([189,328]),
        "Daytona Beach": np.array([1682,829]),
        "Denver": np.array([326,22]),
        "Santa Fe": np.array([227,293]),
        "Abilene": np.array([508,567]),
        "Wichita": np.array([678,196]),
        "OKC": np.array([651, 358]), 
        "Conway": np.array([945, 402]),
        "Memphis": np.array([1090, 400]),
        "Jackson": np.array([1080, 617]),
        "Destin": np.array([1321,761]),
        "Panama City": np.array([1375, 776]),
        "Lexington": np.array([1424, 177]),
        "Springfield IL": np.array([1122, 53]),
        "Columbia": np.array([966, 115]),
        "Joplin": np.array([831, 248]) 
    }
    coordinates, labels = load_coordinates_from_file("graphs/coordinate_graphs/keyboard.txt")

    problem = TravellingSalesmanProblem(labels, coordinates)
    optimization = ACO(problem, 5, 0.5, 0.5, 0.3, 3)
    path, length = optimization.iterate(500)
    for item in path:
        fro, to = item
        print(f"{problem.indices_to_labels[fro]} -> {problem.indices_to_labels[to]}")
    print(f"Total Length: {length}")


if __name__ == "__main__":
    main()
