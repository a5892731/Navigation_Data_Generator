'''
version 2.0
author a5892731
date 2021-03-05
'''



from system.read_data_files import DataImport
from system.functions import deg_to_rad, rad_to_deg
import os
import math

class GeographicObject:
    def __init__(self, FILE_ADDRESS, FOLDER_ADDRESS):
        #latitude szerokość geograficzna (Y)
        #longitude długosć geograficzna (X)

        data = DataImport(FILE_ADDRESS, "dict", FOLDER_ADDRESS)
        self.data = self.convert_data_types(data(), "float")
        self.calculate_radians_for_latitude_and_longitude()

    def __call__(self):
            return self.data

    def convert_data_types(self, data_list, DATA_TYPE):
        output = {}
        for key in data_list:
            value = data_list[key]
            output[key] = self.convert_data_type(value, DATA_TYPE)
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

    def calculate_radians_for_latitude_and_longitude(self):
        self.data["latitude_rad"] = deg_to_rad(self.data["latitude_deg"])
        self.data["longitude_rad"] = deg_to_rad(self.data["longitude_deg"])
#--------------------------------------------------------------------------------------------

class Ship(GeographicObject):
    def __init__(self, FILE_ADDRESS, FOLDER_ADDRESS):
        #latitude szerokość geograficzna (Y)
        #longitude długosć geograficzna (X)

        data = DataImport(FILE_ADDRESS, "dict", FOLDER_ADDRESS)
        self.data = self.convert_data_types(data(), "float")
        self.calculate_radians_for_latitude_and_longitude()
        self.calculate_heading_rad()

    def calculate_heading_rad(self):
        self.data["heading_rad"] = deg_to_rad(self.data["heading_deg"])

#--------------------------------------------------------------------------------------------




if __name__ == "__main__":

    test = 3
    os.chdir("..")

    if test == 1:
        ship = GeographicObject("SHIP_DATA_INPUT.txt", "data_files")
        print(ship())
    if test == 2:
        point = GeographicObject("POINT_DATA_INPUT.txt", "data_files")
        print(point())
    if test == 3:
        ship = GeographicObject("SHIP_DATA_INPUT.txt", "data_files")
        print(ship())
        point = GeographicObject("POINT_DATA_INPUT.txt", "data_files")
        print(point())




    os.chdir("system")

