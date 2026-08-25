from ACO import ACO
from TSP import TravellingSalesmanProblem
import numpy as np 

def main():
    # Sample: [Denver, Albuquerque, Santa Fe, Las Vegas, Elko]
    distances = np.array([
        [0,545,453,971,878],
        [545,0,94,774,1003],
        [453,94,0,838,1019],
        [971,774,839,0,527],
        [878,1003,1019,527,0],
        ])
    labels = ["Denver", "Albuquerque", "Santa Fe", "Las Vegas", "Elko"]
    problem = TravellingSalesmanProblem(labels, distances)
    optimization = ACO(problem, 5, 0.5, 0.5, 0.3, 3)
    path, length = optimization.iterate(500)
    for item in path:
        fro, to = item
        print(f"{problem.indices_to_labels[fro]} -> {problem.indices_to_labels[to]}")
    print(f"Total Length: {length}")


if __name__ == "__main__":
    main()
