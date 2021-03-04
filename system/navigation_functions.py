'''
version 2.0
author a5892731
date 2021-3-04
'''



from system.read_data_files import DataImport
import os
import math

class Object:
    def __init__(self, FILE_ADDRESS, ):
        #latitude  szerokość geograficzna (Y)
        #longitude  długosć geograficzna (X)
        data = DataImport(FILE_ADDRESS, "dict")

        self.data = self.convert_data_types(data())
        self.calculate_radians_for_latitud_and_longitude()

    def __call__(self):
            return self.data

    def calculate_radians_for_latitud_and_longitude(self):
        self.data["latitude_rad"] = self.deg_to_rad(self.data["latitude_deg"])
        self.data["longitude_rad"] = self.deg_to_rad(self.data["longitude_deg"])

#--------------------------------------------------------------------------------------------
    def rad_to_deg(self, rad):
        return rad * 180 / math.pi
    def deg_to_rad(self, deg):
        return deg * math.pi / 180
    def convert_data_types(self, data_list):
        output = {}
        for key in data_list:
            value = data_list[key]
            output[key] = self.convert_data_type(value, "float")
        return output
    def convert_data_type(self, input, data_type):

        if input == "N/A" or input == "None":
            return None
        elif data_type == "str":
            return input
        elif data_type == "int":
            return int(input)
        elif data_type == "float":
            return float(input)



class GeograpficCalculathor:
    def __init__(self, Ship, Point):
        self.ship = Ship
        self.point = Point
        self.calculate_heading_rad()
        self.calculate_distance_from_ship()

        dict = self.ship()
        self.print_dict(dict)
        dict = self.point()
        self.print_dict(dict)

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
        self.calculate_the_resultant_distance()
        self.calculate_fi()

    def calculate_fi(self):  # angle of triangle
        self.point.data["fi_rad"] = math.atan2(self.point.data["distance_from_vessel_lon"], self.point.data["distance_from_vessel_lat"])
        self.point.data["fi_deg"] = self.rad_to_deg(self.point.data["fi_rad"])

    def calculate_the_resultant_distance(self):
        distance_from_vessel = math.sqrt((self.point.data["distance_from_vessel_lat"] ** 2) +
                                         (self.point.data["distance_from_vessel_lon"] ** 2))
        self.point.data["distance_from_vessel"] = distance_from_vessel

    def calculate_heading_rad(self):
        self.ship.data["heading_rad"] = self.deg_to_rad(self.ship.data["heading_deg"])

    def calculate_angle_to_point(self, Point):
        angle_sum_rad = self.ship.data["heading_rad"] + self.point.data["fi_rad"]
        angle_sum_deg = self.ship.rad_to_deg(angle_sum_rad)
        self.ship.data["angle_to_point_rad"] = angle_sum_rad
        self.ship.data["angle_to_point_deg"] = angle_sum_deg

    def rad_to_deg(self, rad):
        return rad * 180 / math.pi
    def deg_to_rad(self, deg):
        return deg * math.pi / 180

    def print_dict(dict):
        for key in dict:
            print("{}: {}".format(key, dict[key]))
        print()


class TestGeograpficCalculathor(GeograpficCalculathor):

    def calculate_distance_from_ship(self, Ship):  # with some small error (oval earth shape) for tests

        earths_equator = 40075704
        earths_equator_per_deg = earths_equator / 360

        x = (self.point.data["longitude_deg"] - self.ship.data["longitude_deg"]) * earths_equator_per_deg

        y = ((self.point.data["latitude_deg"] - self.ship.data["latitude_deg"]) * math.cos(self.point.data["longitude_rad"])) * earths_equator_per_deg

        self.point.data["distance_from_vessel_lat"] = x # in meters
        self.point.data["distance_from_vessel_lon"] = y # in meters
        self.point.calculate_the_resultant_distance()
        self.point.calculate_fi()







if __name__ == "__main__":

    os.chdir("..")

    ship = Object("SHIP_DATA_INPUT.txt")
    point = Object("POINT_DATA_INPUT.txt")
    point_simple = Object("POINT_DATA_INPUT.txt")

    GeograpficCalculathor(ship, point)

    TestGeograpficCalculathor(ship, point_simple)


    os.chdir("system")

