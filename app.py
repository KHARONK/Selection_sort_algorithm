from assignment import get_lat_lon, distance_calculation
from selection_sort import selection_sort


if __name__ == "__main__":
    #place list from map close to Natural History Museum Albuquerque.
    places = ["Sawmill village", "Explora", "Sawmill market", "Casa Esencia", "Albuquerque Hotel",]

    main_place = "Natural History Museum Albuquerque"
    #unsorted distances of the places.
    unsorted_distances = []
    main_place_lat_lon = get_lat_lon(main_place)

    for place in places:
        # Getting the location
        location = get_lat_lon(place)
        #Getting distance from main place.
        distance = distance_calculation(main_place_lat_lon, location)
        #Tuple of place and distance.
        unsorted_distances.append((place, distance))

    #sorting the unsorted distances.
    sorted_distances = selection_sort(unsorted_distances)
    [print(distance[0]) for distance in sorted_distances]
