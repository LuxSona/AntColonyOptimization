import numpy as np
import numpy.typing as npt





def coordinates_to_distance_matrix(city_to_coordinate: dict[str, npt.NDArray[np.float64]]) -> npt.NDArray[np.float64]:
    """Converts a list dictionary list of coordinates to a distance matrix.

    :param city_to_coordinate: A dictionary containing labels matched to numpy coordinates
    :type city_to_coordinate: dict[str, npt.NDArray[np.float64]]
    :return: A distance matrix
    :rtype: npt.NDArray[np.float64]
    """   
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


def load_coordinates_from_file(filename: str) -> tuple[npt.NDArray[np.float64], list[str]]:
    '''
    Loads a set of coordinates from a file.
    The file should be a txt document where each line has the name of the location, followed by a list of numbers (separated by commas) representing the coordinates

    :param filename: The filename
    :type filename: str
    :return: A tuple containing the distance matrix AND the labels
    :rtype: NDArray[float64]
    '''
    city_to_coordinate_dict = {}
    with open(filename) as fp:
        for line in fp.readlines():
            parts = line.split(',')
            label = parts[0]
            coordinates = np.array([float(x) for x in parts[1:]])
            city_to_coordinate_dict[label] = coordinates
    
    return coordinates_to_distance_matrix(city_to_coordinate_dict), list(city_to_coordinate_dict.keys())


def main():
    distances, _ = load_coordinates_from_file("graphs/coordinate_graphs/keyboard.txt")
    print(distances)

if __name__ == "__main__":
    main()
