'''
version 1.0
author: a5892731
date: 2021-03-04


'''

from system.navigation_functions import Object, print_dict
from system.save_data_files import DataExport



#------------------------------------------------------------------------------------------MAIN

if __name__ == "__main__":

    ship = Object("SHIP_DATA_INPUT.txt")
    ship.calculate_radians_for_latitud_and_longitude()
    ship.calculate_heading_rad()

    point = Object("POINT_DATA_INPUT.txt")
    point.calculate_radians_for_latitud_and_longitude()
    point.calculate_distance_from_ship(ship)
    point.calculate_fi()

    ship.calculate_angle_to_point(point)


    print("SHIP: ")
    DataExport(ship.data, "SHIP_DATA_OUTPUT.txt", "dict")
    print_dict(ship())
    print("POINT: ")
    DataExport(point.data, "POINT_DATA_OUTPUT.txt", "dict")
    print_dict(point())