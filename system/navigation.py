'''
version 2.0
author a5892731
date 2021-03-05
'''

import os
import math
from system.geographic_objects import GeographicObject, Ship
from system.functions import deg_to_rad, rad_to_deg

class GeograpficCalculathor:
    def __init__(self, Ship, Point):
        self.ship = Ship
        self.point = Point
        self.calculate_distance_from_ship()
        self.calculate_triangle_angle()
        self.calculate_the_resultant_distance()
        self.calculate_angle_to_point()

        print("Ship: ")
        dict = self.ship()
        self.print_dict(dict)
        print("Point: ")
        dict = self.point()
        self.print_dict(dict)

    def print_dict(self, dict):
        for key in dict:
            print("{}: {}".format(key, dict[key]))
        print()

    def calculate_distance_from_ship(self):        #data camoatibility: World Geodetic System wgs84

        e = 0.081819190842621
        a = 6378137 # [m]

        NC = (a * math.cos(self.point.data["latitude_rad"]) /
              (pow( (1 - e**2 * math.sin(self.point.data["latitude_rad"]**2)) , 1.0/2)))
        M =  (a *(1 - e**2) /
              (pow((1 - e**2 * math.sin(self.point.data["latitude_rad"]**2)), 1.0/2))**3)

        x = NC * (self.point.data["longitude_rad"] - self.ship.data["longitude_rad"])
        y = M  * (self.point.data["latitude_rad"] - self.ship.data["latitude_rad"])

        self.point.data["distance_from_vessel_lat"] = x # in meters
        self.point.data["distance_from_vessel_lon"] = y # in meters

    def calculate_triangle_angle(self):  # angle of triangle
        self.point.data["triangle_angle_rad"] = math.atan2(self.point.data["distance_from_vessel_lat"], self.point.data["distance_from_vessel_lon"])
        self.point.data["triangle_angle_deg"] = rad_to_deg(self.point.data["triangle_angle_rad"])

    def calculate_the_resultant_distance(self):
        distance_from_vessel = math.sqrt((self.point.data["distance_from_vessel_lat"] ** 2) +
                                         (self.point.data["distance_from_vessel_lon"] ** 2))
        self.point.data["distance_from_vessel"] = distance_from_vessel

    def calculate_angle_to_point(self):
        angle_sum_rad = self.point.data["triangle_angle_rad"] - self.ship.data["heading_rad"]
        angle_sum_deg = rad_to_deg(angle_sum_rad)
        self.ship.data["angle_to_point_rad"] = angle_sum_rad
        self.ship.data["angle_to_point_deg"] = angle_sum_deg


if __name__ == "__main__":

    test = 1
    os.chdir("..")

    if test == 1:
        geo = GeograpficCalculathor(Ship("SHIP_DATA_INPUT.txt", "data_files"),
                                    GeographicObject("POINT_DATA_INPUT.txt", "data_files"))



    os.chdir("system")
