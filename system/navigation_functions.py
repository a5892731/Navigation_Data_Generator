from system.read_data_files import DataImport
import os
import math


class Object:
    def __init__(self, FILE_ADDRESS):
        #latitude  szerokość geograficzna (Y)
        #longitude  długosć geograficzna (X)
        data = DataImport(FILE_ADDRESS, "dict")

        self.data = self.convert_data_types(data())

    def __call__(self):
            return self.data

    def calculate_distance_from_ship(self, Ship):        #data camoatibility: World Geodetic System wgs84

        e = 0.081819190842621
        a = 6378137 # [m]
        self.calculate_fi()

        NC = (a * math.cos(self.data["fi_rad"]) / (pow( (1 - e**2 * math.sin(self.data["fi_rad"]**2)) , 1.0/2)))
        M =  (a *(1 - e**2) / (pow( (1 - e**2 * math.sin(self.data["latitude_rad"]**2)) , 1.0/2))**3)

        x = NC * (self.data["longitude_rad"] - Ship.data["longitude_rad"])
        y = M  * (self.data["latitude_rad"] - Ship.data["latitude_rad"])

        self.data["distance_from_vessel_lat"] = x # in meters
        self.data["distance_from_vessel_lon"] = y # in meters
        self.calculate_the_resultant_distance()

    def simplified_calculate_distance_from_ship(self, Ship):  # with some small error (oval earth shape) for tests

        earths_equator = 40075704
        earths_equator_per_deg = earths_equator / 360
        self.calculate_fi()

        x = (self.data["longitude_deg"] - Ship.data["longitude_deg"]) * earths_equator_per_deg

        y = ((self.data["latitude_deg"] - Ship.data["latitude_deg"]) * math.cos(self.data["longitude_rad"])) * earths_equator_per_deg

        self.data["distance_from_vessel_lat"] = x # in meters
        self.data["distance_from_vessel_lon"] = y # in meters
        self.calculate_the_resultant_distance()

    def convert_data_types(self, data_list):
        output = {}

        for key in data_list:
            value = data_list[key]

            if key == "latitude_deg":
                output["latitude_deg"] = self.convert_data_type(value, "float")
            elif key == "latitude_rad":
                output["latitude_rad"] = self.convert_data_type(value, "float")
            elif key == "longitude_deg":
                output["longitude_deg"] = self.convert_data_type(value, "float")
            elif key == "longitude_rad":
                output["longitude_rad"] = self.convert_data_type(value, "float")
            elif key == "distance_from_vessel":
                output["distance_from_vessel"] = self.convert_data_type(value, "float")
            elif key == "distance_from_vessel_lat":
                output["distance_from_vessel_lat"] = self.convert_data_type(value, "float")
            elif key == "distance_from_vessel_lon":
                output["distance_from_vessel_lon"] = self.convert_data_type(value, "float")
            elif key == "fi_rad":
                output["fi_rad"] = self.convert_data_type(value, "float")
            elif key == "fi_deg":
                output["fi_deg"] = self.convert_data_type(value, "float")
            elif key == "heading_rad":
                output["heading_rad"] = self.convert_data_type(value, "float")
            elif key == "heading_deg":
                output["heading_deg"] = self.convert_data_type(value, "float")
            elif key == "angle_to_point_rad":
                output["angle_to_point_rad"] = self.convert_data_type(value, "float")
            elif key == "angle_to_point_deg":
                output["angle_to_point_deg"] = self.convert_data_type(value, "float")

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

    def calculate_radians_for_latitud_and_longitude(self):
        self.data["latitude_rad"] = self.deg_to_rad(self.data["latitude_deg"])
        self.data["longitude_rad"] = self.deg_to_rad(self.data["longitude_deg"])

    def calculate_the_resultant_distance(self):
        distance_from_vessel = math.sqrt((self.data["distance_from_vessel_lat"]**2) +
                                         (self.data["distance_from_vessel_lon"]**2))
        self.data["distance_from_vessel"] = distance_from_vessel


    def calculate_heading_rad(self):
        self.data["heading_rad"] = self.deg_to_rad(self.data["heading_deg"])

    def calculate_fi(self):
        self.data["fi_rad"] = math.atan2(self.data["distance_from_vessel_lon"], self.data["distance_from_vessel_lat"])
        self.data["fi_deg"] = self.rad_to_deg(self.data["fi_rad"])

    def rad_to_deg(self, rad):
        return rad * 180 / math.pi

    def deg_to_rad(self, deg):
        return deg * math.pi / 180

    def calculate_angle_to_point(self, Point):
        angle_sum_rad = self.data["heading_rad"] + Point.data["fi_rad"]
        angle_sum_deg = self.rad_to_deg(angle_sum_rad)
        self.data["angle_to_point_rad"] = angle_sum_rad
        self.data["angle_to_point_deg"] = angle_sum_deg

def print_dict(dict):
    for key in dict:
        print("{}: {}".format(key, dict[key]))
    print()


if __name__ == "__main__":

    os.chdir("..")

    ship = Object("SHIP_DATA_INPUT.txt")
    ship.calculate_radians_for_latitud_and_longitude()
    ship.calculate_heading_rad()
    point = Object("POINT_DATA_INPUT.txt")
    point.calculate_radians_for_latitud_and_longitude()
    point_simple = Object("POINT_DATA_INPUT.txt")
    point_simple.calculate_radians_for_latitud_and_longitude()

    print("SHIP: ")
    print_dict(ship())
    print("TEST SIMPLIFIED POINT: ")
    point_simple.simplified_calculate_distance_from_ship(ship)

    print_dict(point_simple())
    print("POINT: ")
    point.calculate_distance_from_ship(ship)

    print_dict(point())

    os.chdir("system")

