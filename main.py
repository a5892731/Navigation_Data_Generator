'''
version 2.0
author: a5892731
date: 2021-03-05

for tests:
https://pl.distance.to/56.237244700410336,19.3786995097812/55.54728069864083,19.93892661954635
...
more in file:
SAVED_DATA.txt
'''


from system.save_data_files import DataExport
from system.navigation import GeograpficCalculathor
from system.geographic_objects import GeographicObject, Ship


#------------------------------------------------------------------------------------------MAIN

if __name__ == "__main__":

    ship = Ship("SHIP_DATA_INPUT.txt", "data_files")
    point = GeographicObject("POINT_DATA_INPUT.txt", "data_files")

    geo = GeograpficCalculathor(ship, point)

    DataExport(ship(), "SHIP_DATA_OUTPUT.txt", "dict")
    DataExport(point(), "POINT_DATA_OUTPUT.txt", "dict")
