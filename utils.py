import numpy as np
import numpy.typing as npt





def coordinates_to_distance_matrix(city_to_coordinate: dict[str, npt.NDArray[np.float64]]) -> npt.NDArray[np.float64]:
    n = len(city_to_coordinate)
    distance_matrix : npt.NDArray[np.float64] = np.zeros((n,n))
    cities = city_to_coordinate.keys()
    for i, city_i in enumerate(cities):
        for j, city_j in enumerate(cities):
            if city_i == city_j:
                continue
            else:
                distance_matrix[i,j] = np.linalg.norm((city_to_coordinate[city_i]) - (city_to_coordinate[city_j]))
    return distance_matrix

def main():
    cities = {
        "alpha": np.array([1,1]),
        "beta": np.array([2,2]),
        "gamma": np.array([-1,1]),
    }

    distances = coordinates_to_distance_matrix(cities)
    print(distances)

if __name__ == "__main__":
    main()
